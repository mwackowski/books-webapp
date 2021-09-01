import asyncio
import json
import math
import os
import sqlite3
from pathlib import Path

import aiohttp
import numpy as np
import pandas as pd
import requests


def create_search_parameters(cleaned_data):
    search_parameters = ''
    if cleaned_data['volume']:
        search_parameters += '+'.join(cleaned_data['volume'].split()) + '+'
    search_parameters = search_parameters + '+'.join([f'{k}:{"+".join(str(v).split())}' for k, v in cleaned_data.items() if k != 'volume' and v])
    return search_parameters

def extract_values(book):
    d = {}
    keys = ['title', 'authors', 'pageCount', 'imageLinks', 'language', 'industryIdentifiers', 'publishedDate']
    isbns = ['ISBN_10', 'ISBN_13']
    for x in keys:
        try:
            b = book['volumeInfo']
            if x == 'imageLinks':
                d[x] = b[x]['thumbnail']
            elif x == 'industryIdentifiers':
                for i in b[x]:
                    if i['type'] in isbns:
                        d[i['type']] = i['identifier']
            elif x == 'authors':
                d[x] = ', '.join(b[x])
            else:
                d[x] = b[x]
        except KeyError:
            d[x] = None
    return d

def query_api(search_parameters):

    async def main():
        async with  aiohttp.ClientSession() as session:    
            tasks = []
            for i in range(1, iterations):
                task = asyncio.ensure_future(send_request(session, i*40, search_parameters))
                tasks.append(task)
            results = await asyncio.gather(*tasks)
            return results

    async def send_request(session, index, search_parameters):
        url = f'https://www.googleapis.com/books/v1/volumes?q={search_parameters}&maxResults=40&startIndex={str(index)}'
        async with session.get(url, headers=header) as response:
            result_data = await response.json()
            return result_data

    header = {'Accept-Encoding': 'gzip', 'accept-language': '*'}
    url = f'https://www.googleapis.com/books/v1/volumes?q={search_parameters}&maxResults=40&startIndex=0'
    print(url)
    r = requests.get(url, headers=header)

    iterations = math.floor(r.json()['totalItems']/40)
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    outcome = loop.run_until_complete(main())
    loop.close()
    outcome = [r.json()]+ outcome
    return outcome

def insert_to_db(books):
    path = os.path.join(Path(__file__).resolve().parent.parent, 'db.sqlite3')
    con = sqlite3.connect(path)
    execute = []
    cols_api = ['title', 'authors', 'publishedDate', 'ISBN_10', 'ISBN_13', 'pageCount', 'imageLinks', 'language', 'industryIdentifiers']
    cols_model = ['id', 'title', 'author', 'published_date', 'isbn10', 'isbn13', 'pages', 'front_page', 'language', 'industry_identifiers']
    df = pd.DataFrame(columns=cols_api)

    for book in books:
        try:
            for b in book['items']:
                execute.append(extract_values(b))
        except KeyError:
            print(book)
            
    df = pd.concat([df, pd.DataFrame(execute)], ignore_index=True)
    df.reset_index(inplace=True)
    if len(df) > 0:
        df.pageCount = df.pageCount.astype('Int64')
        df = df.where(pd.notnull(df), None)
        last_id = pd.read_sql_query('select * from catalogue_catalogue', con).id.max()
        if last_id:
            df.iloc[:,0] = df.iloc[:,0] + last_id + 1
        df.columns = df.columns.to_series().map({x[0]:x[1] for x in zip(['index']+cols_api, cols_model)})
        df.to_sql('catalogue_catalogue', con, if_exists='append', index=False)
    return len(df)

def send_query(cleaned_data):
    books = query_api(create_search_parameters(cleaned_data))
    books_len = insert_to_db(books)
    return books_len
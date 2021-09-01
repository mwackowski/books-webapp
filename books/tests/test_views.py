from django.test import TestCase, Client
from django.urls import reverse
from catalogue.models import Catalogue


class TestViews(TestCase):
    
    def setUp(self):
        self.client = Client()
        self.list_url = reverse('book-list')
        self.create_url = reverse('book-create')

    def create_book(self, title, author, published_date, language):
        new_book = Catalogue.objects.create(
            title=title,
            author=author,
            published_date=published_date,
            language=language
        )
        return new_book

    def test_cat_list(self):
        response = self.client.get(self.list_url)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'books_list.html')
        self.assertTemplateNotUsed(response, 'book_list.html')

    def test_cat_create(self):
        response = self.client.post(self.create_url, {'title': 'testTtitle', 
                        'author': 'Mateusz W', 
                        'published_date': '2021', 
                        'language': 'pl'}
        )
        self.assertEquals(response.status_code, 302)
        self.assertEquals(Catalogue.objects.last().title, "testTtitle")
        self.assertNotEquals(Catalogue.objects.last().published_date, "2020")

    def test_cat_update(self):
        book = self.create_book('Bad bad Hobbit', 'Tolkien', '2000', 'en')
        response = self.client.post(reverse('book-update', args= (book.id,)),
                                    {'title': 'Good Hobbit',
                                    'author': 'Tolkien',
                                    'published_date': '2000',
                                    'language': 'en'}
        )
        self.assertEquals(response.status_code, 302)
        self.assertEquals(Catalogue.objects.last().title, 'Good Hobbit')

    def test_cat_delete(self):
        book = self.create_book('Bad bad Hobbit', 'Tolkien', '2000', 'en')
        response = self.client.delete(reverse('book-delete', args= (book.id,)),)
        self.assertEquals(response.status_code, 302)
        self.assertEquals(Catalogue.objects.count(), 0)

    def test_cat_delete_bad_id(self):
        self.create_book('Bad bad Hobbit', 'Tolkien', '2000', 'en')
        response = self.client.delete(reverse('book-delete', args= (0,)),)
        self.assertEquals(response.status_code, 404)
        self.assertEquals(Catalogue.objects.count(), 1)

    def test_req_form_view(self):
        response = self.client.post(reverse('book-request'), {'title': 'Good Hobbit','volume': 'Kolorowanki',})
        self.assertEquals(response.status_code, 200)
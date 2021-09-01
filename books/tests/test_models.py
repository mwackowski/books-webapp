from django.test import TestCase
from catalogue.models import Catalogue
from django.db.utils import IntegrityError


class TestModels(TestCase):

    def create_book(self, title, author, published_date, language):
        new_book = Catalogue.objects.create(
            title=title,
            author=author,
            published_date=published_date,
            language=language
        )
        return new_book

    def setUp(self):
        self.book = self.create_book('Wiedźmin', 'Sapkowski', '2000', 'pl')
    
    def test_id_assigned_on_creation(self):
        self.assertEquals(self.book.id, Catalogue.objects.last().id)

    """This method should actually throw some db errors as 'title' is declared as VARCHAR(100)
    but sqlite treats it as a TEXT instead with no length limitations
    https://www.sqlite.org/faq.html 
    (9) What is the maximum size of a VARCHAR in SQLite?
    SQLite does not enforce the length of a VARCHAR. You can declare a VARCHAR(10) and 
    SQLite will be happy to store a 500-million character string there. And it will keep 
    all 500-million characters intact. Your content is never truncated. SQLite understands 
    the column type of "VARCHAR(N)" to be the same as "TEXT", regardless of the value of N.
    """
    def test_long_field(self):
        long_title = 'a'*150
        new_book = self.create_book(long_title, '', '', '')
        self.assertEquals(new_book.id, 2)
        self.assertEquals(new_book.title, long_title)

    def test_notnull_field(self):
        with self.assertRaises(IntegrityError) as context:
            self.create_book(None, '', '', '')
        self.assertTrue('NOT NULL constraint failed' in str(context.exception))
        
    
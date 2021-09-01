from django.test import TestCase, Client
from django.urls import reverse
from catalogue.forms import RequestForm


class TestForms(TestCase):

    def test_req_form_filled(self):
        form = RequestForm(data={'volume': 'test Volume', 
                        'intitle': 'Some funny title', 
                        'inauthor': 'Mateusz W'}
        )
        self.assertEquals(form.data['volume'], 'test Volume')
        self.assertEquals(form.data['intitle'], 'Some funny title')
        self.assertNotEquals(form.data['inauthor'], 'Mateusz')

    def test_req_form_empty(self):
        form = RequestForm(data={})
        self.assertFalse(form.is_valid())
        self.assertEquals(
            form.errors['__all__'], ["At least one of the fields should be filled"]
        )
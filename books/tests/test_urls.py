from django.test import SimpleTestCase
from django.urls import reverse, resolve
from catalogue.views import (
    CatalogueListView, 
    CatalogueCreateView,
    CatalogueUpdateView,
    CatalogueDeleteView,
    requestForm
)


class TestUrls(SimpleTestCase):

    def test_list_url_resolves(self):
        url = reverse('book-list')
        self.assertEquals(resolve(url).func.view_class, CatalogueListView)    

    def test_create_url_resolves(self):
        url = reverse('book-create')
        self.assertEquals(resolve(url).func.view_class, CatalogueCreateView)   
        
    def test_update_url_resolves(self):
        url = reverse('book-update', args=(1,))
        self.assertEquals(resolve(url).func.view_class, CatalogueUpdateView)   

    def test_delete_url_resolves(self):
        url = reverse('book-delete', args=(2,))
        self.assertEquals(resolve(url).func.view_class, CatalogueDeleteView)    

    def test_request_url_resolves(self):
        url = reverse('book-request')
        self.assertEquals(resolve(url).func, requestForm)

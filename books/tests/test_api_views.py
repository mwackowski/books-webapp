from api.serializers import CatalogueSerializer
from catalogue.models import Catalogue
from django.contrib.auth.models import User
from django.urls import reverse
from rest_framework.test import APIClient, APITestCase


class TestApiViews(APITestCase):

    def setUp(self):
        self.client = APIClient()

    def test_cat_list(self):
        response = self.client.get(reverse('catalogue:list'))
        self.assertEquals(response.status_code, 200)

    def test_cat_detail(self):
        book = Catalogue.objects.create(title='Test API title', language='pl')
        response = self.client.get(reverse('catalogue:detail', args=(book.id,)))
        self.assertEquals(response.data["title"], book.title)
        self.assertNotEquals(response.data["language"], 'en')

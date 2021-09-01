from django.test import SimpleTestCase
from django.urls import reverse, resolve
from rest_framework.test import APITestCase
from api.views import (
    api_detail_view,
    ApiBooksListView
)


class TestApiUrls(APITestCase):

    def test_list_url_resolves(self):
        url = reverse('catalogue:list')
        self.assertEquals(resolve(url).func.view_class, ApiBooksListView)

    def test_list_url_resolves(self):
        url = reverse('catalogue:detail', args=(1,))
        self.assertEquals(resolve(url).func, api_detail_view)
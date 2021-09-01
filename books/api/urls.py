from django.conf.urls import url
from django.urls import path

from .views import ApiBooksListView, api_detail_view


app_name = 'catalogue'

urlpatterns = [
    path('<id>/', api_detail_view, name='detail'),
    path('', ApiBooksListView.as_view(), name='list'), 
]

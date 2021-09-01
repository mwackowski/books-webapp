"""books URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.urls.conf import include
from catalogue.views import (
    CatalogueListView, 
    CatalogueDetailView, 
    CatalogueCreateView, 
    CatalogueDeleteView, 
    CatalogueUpdateView, 
    requestForm,
    apiDocs
    )

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', CatalogueListView.as_view(), name='book-list'),
    path('<int:id>', CatalogueDetailView.as_view(), name='book-detail'),
    path('create/', CatalogueCreateView.as_view(), name='book-create'), 
    path('update/<int:id>/', CatalogueUpdateView.as_view(), name='book-update'),
    path('delete/<int:id>/', CatalogueDeleteView.as_view(), name='book-delete'),
    path('search', requestForm, name='book-request'),
    path('api', apiDocs, name='api-docs'),
    #REST FRAMEWORK
    path('api/books/', include('api.urls', 'books_api')),
]

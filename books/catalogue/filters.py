import django
import django_filters
from django_filters.filters import CharFilter, DateFilter
from .models import Catalogue
from django import forms


class TableFilter(django_filters.FilterSet):
    title = django_filters.CharFilter(lookup_expr='icontains', widget=forms.TextInput(
        attrs={ 
                'placeholder': 'Search by title...',
                'class': 'form-control'}
    ))
    author = django_filters.CharFilter(lookup_expr='icontains', widget=forms.TextInput(
        attrs={ 
                'placeholder': 'Search by author...',
                'class': 'form-control'}
    ))
    language = django_filters.CharFilter(lookup_expr='icontains', widget=forms.TextInput(
        attrs={ 
                'placeholder': 'Search by language...',
                'class': 'form-control'}
    ))
    start_date = DateFilter(field_name="published_date", lookup_expr='gte', widget=forms.TextInput(
        attrs={ 
                'placeholder': 'Published date starting...',
                'class': 'form-control',
                'type': 'date'}
    ))
    end_date = DateFilter(field_name="published_date", lookup_expr='lte', widget=forms.TextInput(
        attrs={ 
                'placeholder': 'Published date ending...',
                'class': 'form-control',
                'type': 'date'}
    ))
    
    class Meta:
        model = Catalogue
        fields = []



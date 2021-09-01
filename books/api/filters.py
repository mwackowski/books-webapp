import django_filters
from catalogue.models import Catalogue
from rest_framework import filters

#source:
#https://stackoverflow.com/questions/45296939/how-can-i-create-a-partial-search-filter-in-django-rest-framework
class ContactFilter(filters.BaseFilterBackend):
    allowed_fields = ['title', 'author', 'language', 'published_date']

    def filter_queryset(self, request, queryset, view):
        fltr = {}
        for param in request.query_params:
            for fld in self.allowed_fields:
                if param.startswith(fld):
                    fltr[param] = request.query_params[param]
        return queryset.filter(**fltr)

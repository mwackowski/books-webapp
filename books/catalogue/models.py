from django.db import models
from django.urls import reverse


class Catalogue(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100, null=False, blank=False)
    author = models.CharField(max_length=100, null=True)
    # charfield instead of datefield due to data malfunction, i.e. 200? in published_date field for ISBN13 9788373377899
    published_date = models.CharField(null=True, blank=True, max_length=10)  
    isbn10 = models.CharField(max_length=13, null=True, blank=True)
    isbn13 = models.CharField(max_length=13, null=True, blank=True)
    pages = models.IntegerField(null=True, blank=True)
    front_page = models.CharField(max_length=500, null=True, blank=True)
    language = models.CharField(max_length=4)
    industry_identifiers = models.CharField(max_length=15, null=True, blank=True)
    def get_absolute_url(self):
        return reverse("book-list")
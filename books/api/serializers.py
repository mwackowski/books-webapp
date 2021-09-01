from rest_framework import serializers
from catalogue.models import Catalogue


class CatalogueSerializer(serializers.ModelSerializer):
    class Meta:
        model = Catalogue
        fields = '__all__'
from catalogue.models import Catalogue
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.generics import ListAPIView
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response

from .filters import ContactFilter
from .serializers import CatalogueSerializer


@api_view(['GET',])
def api_detail_view(request, id):
    try:
        book = Catalogue.objects.get(id=id)
    except Catalogue.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = CatalogueSerializer(book)
        return Response(serializer.data)

class PaginateView(PageNumberPagination):
    page_size = 5
    page_size_query_param = 'page_size'
    max_page_size = 20

class ApiBooksListView(ListAPIView):
    queryset = Catalogue.objects.all()
    serializer_class = CatalogueSerializer
    pagination_class = PaginateView
    filter_backends = [ContactFilter,]

  #TODO - fix
  #...\pagination.py:200: UnorderedObjectListWarning: 
  # Pagination may yield inconsistent results with an unordered object_list: <class 'catalogue.models.Catalogue'> QuerySet.

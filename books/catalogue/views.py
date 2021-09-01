from django.shortcuts import render, get_object_or_404
from django.views.generic import (
    CreateView,
    DetailView,
    ListView,
    UpdateView,
    DeleteView)
from django.urls import reverse
from django_filters.views import FilterView
from .forms import CatalogueModelForm, RequestForm
from .models import Catalogue
from .filters import TableFilter
from db_functions.query_api import send_query


class CatalogueListView(ListView):
    model = Catalogue
    template_name = 'books_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filter'] = TableFilter(self.request.GET, queryset=self.get_queryset())
        return context

class CatalogueDetailView(DetailView):
    template_name = 'books_details.html'

    def get_object(self):
        id_ = self.kwargs.get('id')
        return get_object_or_404(Catalogue, id=id_)

class CatalogueCreateView(CreateView):
    template_name = 'books_create.html'
    form_class = CatalogueModelForm
    queryset = Catalogue.objects.all()
    success_url = '/'

    def form_valid(self, form):
        # print(form.cleaned_data)
        return super().form_valid(form)

class CatalogueUpdateView(UpdateView):
    template_name = 'books_create.html'
    form_class = CatalogueModelForm
    queryset = Catalogue.objects.all()

    def get_object(self):
        id_ = self.kwargs.get('id')
        return get_object_or_404(Catalogue, id=id_)

    def form_valid(self, form):
        return super().form_valid(form)

    def get_success_url(self) -> str:
        return reverse('book-list')

class CatalogueDeleteView(DeleteView):
    template_name = 'books_delete.html'
    # success_url = '/'
    def get_object(self):
        id_ = self.kwargs.get('id')
        return get_object_or_404(Catalogue, id=id_)

    def get_success_url(self) -> str:
        return reverse('book-list')

def requestForm(request):
    form = RequestForm(request.POST or None)
    if form.is_valid():
        records = send_query(form.cleaned_data)
        context= {'form': form, 'records': records}
    else:
        context= {'form': form}
    return render(request, 'books_request.html', context)

def apiDocs(request):
    return render(request, "api_docs.html")

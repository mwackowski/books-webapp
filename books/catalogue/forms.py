from .models import Catalogue
from django import forms


class CatalogueModelForm(forms.ModelForm):

    class Meta:
        model = Catalogue
        fields = '__all__'

    def clean_isbn10(self, *args, **kwargs):
        # print(self.cleaned_data)
        isbn10 = self.cleaned_data.get('isbn10')
        if len(str(isbn10)) != 10 and isbn10:
            raise forms.ValidationError('Valid ISBN10 should be 10-digit long')
        return isbn10

    def clean_isbn13(self, *args, **kwargs):
        # print(self.cleaned_data)
        isbn13 = self.cleaned_data.get('isbn13')
        if len(str(isbn13)) != 13 and isbn13:
            raise forms.ValidationError('Valid ISBN13 should be 13-digit long')
        return isbn13

class RequestForm(forms.Form):
    volume = forms.CharField(required=False)
    intitle = forms.CharField(required=False, label='In title')
    inauthor = forms.CharField(required=False)
    inpublisher = forms.CharField(required=False)
    subject = forms.CharField(required=False)
    isbn  = forms.IntegerField(required=False)
    lccn = forms.CharField(required=False)
    oclc = forms.CharField(required=False)

    def clean(self):
        s = self.cleaned_data
        if not any([str(v).strip() for v in list(s.values()) if v is not None]):
            raise forms.ValidationError('At least one of the fields should be filled')
        return s

from django import forms

from webapp.models import  Product


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['title', 'description', 'price', 'image', 'category', 'remaining']

class SearchForm(forms.Form):
    search = forms.CharField(label='Поиск продукта', max_length=100, required=False, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Введите название марки машины...'}))
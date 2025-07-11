from django.shortcuts import render, redirect, get_object_or_404

from webapp.forms import ProductForm, SearchForm
from webapp.models import Product, Category


# Create your views here.
def index(request):
    form = SearchForm(request.GET or None)
    products = Product.objects.order_by('category', 'title').filter(remaining__gt=1)
    categories = Category.objects.all()
    if form.is_valid():
        search = form.cleaned_data.get('search')
        if search:
            products = products.filter(title__icontains=search)
    return render(request, 'index.html', {"products" : products, "form" : form, "categories": categories})


def categories_add(request):
    if request.method == "POST":
        name = request.POST.get('name')
        content = request.POST.get('content')
        category = Category.objects.create(name=name, content=content)
        return redirect('categories_view')
    else:
        categories = Category.objects.all()
        return render(request, 'categories_add.html', {'categories': categories})

def categories_view(request):
    categories = Category.objects.all()
    return render(request, 'categories_view.html', {'categories': categories})


def category_edit_view(request, pk):
    category = get_object_or_404(Category, pk=pk)
    if request.method == "POST":
        category.name = request.POST.get('name')
        category.content = request.POST.get('content')
        category.save()
        return redirect('categories_view')
    else:
        return render(request, 'category_edit.html', {'category': category})


def category_delete(request, pk):
    category = get_object_or_404(Category, pk=pk)
    category.delete()
    return redirect('categories_view')
def products_add(request):
    if request.method == "POST":
        form = ProductForm(request.POST)
        if form.is_valid():
            product = form.save()
            return redirect('product_details', pk=product.pk)
        else:
            return render(request, 'products_add.html', {'form': form})
    else:
        form = ProductForm()
        return render(request, 'products_add.html', {'form': form})



def product_edit_view(request, pk):
    product = get_object_or_404(Product, pk=pk)
    if request.method == "POST":
        form = ProductForm(request.POST, instance=product)
        if form.is_valid():
            product= form.save()
            return redirect('product_details', pk=product.pk)
        else:
            return render(request, 'product_edit.html', {'form': form})
    else:
        form = ProductForm(instance=product)
        return render(request, 'product_edit.html', {'form': form})


def product_delete(request, pk):
    product = get_object_or_404(Product, pk=pk)
    product.delete()
    return redirect('index')

def product_details (request, *args, pk, **kwargs ):
    product = get_object_or_404(Product, pk=pk)
    return render(request, 'product_details.html', {"product": product})
def products_category(request,  *args, slug, **kwargs ):
    category = get_object_or_404(Category, slug=slug)
    products = Product.objects.filter(category=category, remaining__gt=0).order_by('title')

    form = SearchForm(request.GET or None)
    if form.is_valid():
        search = form.cleaned_data.get('search')
        if search:
            products = products.filter(title__icontains=search)
    return render(request, 'products_category.html', {'category': category, 'products': products, 'form': form})






from django.shortcuts import render, redirect, get_object_or_404

from webapp.models import Product, Category


# Create your views here.
def index(request):
    products = Product.objects.order_by('-id')
    return render(request, 'index.html', {"products" : products})


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
        title = request.POST.get('title')
        description = request.POST.get('description')
        price = request.POST.get('price')
        image = request.POST.get('image')
        category_id = request.POST.get('category_id')
        product = Product.objects.create(title=title, price=price, image=image, description=description, category_id=category_id)
        return redirect('product_details', pk=product.pk)
    else:
        categories = Category.objects.all()
        return render(request, 'products_add.html', {'categories': categories})

def product_details (request, *args, pk, **kwargs ):
    product = get_object_or_404(Product, pk=pk)
    return render(request, 'product_details.html', {"product": product})

def product_edit_view(request, pk):
    product = get_object_or_404(Product, pk=pk)
    if request.method == "POST":
        product.title = request.POST.get('title')
        product.description = request.POST.get('description')
        product.price = request.POST.get('price')
        product.image = request.POST.get('image')
        product.category_id = request.POST.get('category_id')
        product.save()
        return redirect('product_details', pk=product.pk)
    else:
        categories = Category.objects.all()
        return render(request, 'product_edit.html', {'product': product, 'categories': categories})


def product_delete(request, pk):
    product = get_object_or_404(Product, pk=pk)
    product.delete()
    return redirect('index')






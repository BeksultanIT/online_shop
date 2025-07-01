from itertools import product

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
        return redirect('index', {"category":category})
    else:
        categories = Category.objects.all()
        return render(request, 'categories_add.html', {'categories': categories})

def products_add(request):
    if request.method == "POST":
        title = request.POST.get('title')
        description = request.POST.get('description')
        category = request.POST.get('category')
        price = request.POST.get('price')
        image = request.POST.get('image')
        category_id = request.POST.get('content')
        product = Product.objects.create(title=title, price=price, image=image, category=category, description=description, category_id=category_id)
        return redirect('product_details', pk=product.pk)
    else:
        categories = Category.objects.all()
        return render(request, 'products_add.html', {'categories': categories})

def product_details (request, *args, pk, **kwargs ):
    product = get_object_or_404(Product, pk=pk)
    return render(request, 'product_details.html', {'product': product})






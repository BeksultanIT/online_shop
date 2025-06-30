from django.shortcuts import render, redirect, get_object_or_404

from webapp.models import Product


# Create your views here.
def index(request):
    return render(request, 'index.html',)

def products_add(request):
    if request.method == "POST":
        title = request.POST.get('title')
        price = request.POST.get('price')
        image = request.POST.get('image')
        category = request.POST.get('category')
        description = request.POST.get('description')
        product = Product.objects.create(title=title, price=price, image=image, category=category, description=description)
        return redirect('product_detail', pk=product.pk)


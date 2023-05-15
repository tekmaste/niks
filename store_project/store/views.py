from django.shortcuts import render
from django.http import HttpResponse
from .models import Product, Category



def build_layout(lst,cols):
    array = []
    for i in range(0, len(lst), cols):
        array.append(lst[i:i+cols])
        
    return array


def product_list(request):
    products = Product.objects.all()
    categories = Category.objects.all()
    return render(request, "store/index.html", context={"product_list": build_layout(products, 3), "cats": categories})
    

def product_detail(request, pk):
    product = Product.objects.get(pk = pk)
    categories = Category.objects.all()
    return render(request, "store/product_detail.html", context={"product": product, "cats": categories})
    
def category_detail(request, pk):
    categories = Category.objects.all()
    category = Category.objects.get(pk = pk)
    products = category.products.all()
    return render(request, "store/category_detail.html", context={"cats": categories, "product_list": build_layout(products, 3), "category": category})
    

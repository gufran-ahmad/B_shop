from django.shortcuts import render
from numpy import product

from .models.product import Product
from .models.category import Category
# Create your views here.
def index(request):
    products = None
    category = Category.get_all_categories();
    categoryID = request.GET.get('category')
    if categoryID:
        products = Product.get_all_products_by_categoryid(categoryID)
    else:
        products = Product.get_all_products();
    # print(product)
    data = {}
    data['products'] = products
    data['categories'] = category
    return render(request,'index.html',data)

def signup(request):
    return render(request,'signup.html')

def login(request):
    return render(request,'login.html')

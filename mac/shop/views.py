from django.shortcuts import render
from .models import Product
from django.http import HttpResponse
from math import ceil
# Create your views here.
def index(request):
    # products = Product.objects.all()
    # print(products)
    # n = len(products)
    # nSlides = n//4 + ceil((n/4)-(n//4))
    # params={'no_of_slides':nSlides,'range':range(1,nSlides),'product':products}
    # allProds = [[products,range(1,nSlides),nSlides],[products,range(1,nSlides),nSlides]]
    allProds = []
    catProds = Product.objects.values('category','id')
    cats = {item['category'] for item in catProds}
    for cat in cats:
        prod = Product.objects.filter(category=cat)
        n = len(prod)
        nSlides = n // 4 + ceil((n / 4) - (n // 4))
        allProds.append([prod,range(1,nSlides),nSlides])

    params = {'allProds':allProds}
    return render(request,"shop/index.html",params)
def about(request):
    return render(request, "shop/about.html")
def contact(request):
    return HttpResponse("we are at contact")
def tracker(request):
    return HttpResponse("we are at tracker")
def search(request):
    return HttpResponse("we are at search")
def productview(request):
    return HttpResponse("we are at prodview")
def checkout(request):
    return HttpResponse("we are at checkout")

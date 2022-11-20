import re
from django.shortcuts import render
from django.http import HttpResponse
from welcome import models

# Create your views here.
def index(request):
    return render(request, 'home.html')

def product(request):
    products = models.Product.objects.all()
    return render(request, 'index.html',locals())

def detail(request, id):
    try:
        product = models.Product.objects.get(id = id)
        images = models.PPhoto.objects.filter(product = product)
    except:
        pass
    return render(request, 'detail.html', locals())
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

def login(request):
    try:
        urid = request.GET['user_id']
        urpass = request.GET['user_pass']
    except:
        urid = None
    
    if(urid != None and urpass == '12345'):
        verified = True
    else:
        verified = False
    return render(request, 'login.html', locals())

def choice_dick(request):
    return render(request, 'choice_dick.html', locals())
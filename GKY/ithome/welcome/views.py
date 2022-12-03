import re
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from welcome import models
from django.core import serializers
# Create your views here.
from welcome.models import Music

from welcome.serializers import MusicSerializer
# rest_framework provide
from rest_framework import viewsets


# Create your views here.
class MusicViewSet(viewsets.ModelViewSet):
    queryset = Music.objects.all()
    serializer_class = MusicSerializer

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

def get_dick_api(request):
    dick = models.Product.objects.all()
    data = serializers.serialize('json', dick)
    return JsonResponse({'data':data})

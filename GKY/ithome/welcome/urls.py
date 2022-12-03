"""ithome URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
# from django.conf.urls import url, include
from django.contrib import admin
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
# generate five url address
router.register(r'music', views.MusicViewSet)

urlpatterns = [
    path('', views.index, name = 'home-url'),
    path('product/', views.product),
    path('detail/<int:id>',views.detail, name = 'detail-url'),
    path('login/', views.login),
    path('choice_dick/', views.choice_dick, name = 'choiceDick-url'),
    path('api/dick', views.get_dick_api),
    path('api/',include(router.urls))
]

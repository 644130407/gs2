"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.urls import path

from article import views

urlpatterns = [
    path('articlelist/', views.articlelist),
    path('articleadd/', views.articleadd),
    path('articleedit/', views.articleedit),
    path('articledel/', views.articledel),
    path('init/', views.init),

    path('typelist/', views.typelist),
    path('typeedit/', views.typeedit),
    path('typedel/', views.typedel),
    path('typeadd/', views.typeadd),
    path('columnlist/', views.columnlist),
    path('columnadd/', views.columnadd),
    path('columnedit/', views.columnedit),
    path('columndel/', views.columndel),
    path('contentlist/', views.contentlist),
    path('subcontentlist/', views.subcontentlist),
    path('contentadd/', views.contentadd),
    path('contentedit/', views.contentedit),
    path('contentdel/', views.contentdel),

    path('uploadbg/', views.uploadbg),

    path('testadd/', views.testadd)
]

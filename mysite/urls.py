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
from django.urls import path, include, re_path

from login import views

from django.conf import settings
from django.conf.urls.static import static
from front import views as frontviews

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', include('login.urls')),
    path('article/', include('article.urls')),
    path('summernote/', include('django_summernote.urls')),
    path('formtest/', include('formtest.urls')),
    path('front/', include('front.urls')),
    path('test/', frontviews.test),
    path('gs/', frontviews.gs),
    re_path(r'^$', frontviews.index)
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

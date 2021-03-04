"""telecom URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.conf.urls import url
from product.views import *
from home.views import *
from default.views import *
from django.conf.urls.static import static

from telecom import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name="index"),
    path('search/', search_filter, name="search_filter"),
    path('create/post', post_create, name="post_create"),
    path('product/ajax/', get_product_ajax, name="get_product_ajax"),
    path('product/<slug:category>/<slug:name>/', product_index, name="product_index"),
    path('product/<slug:category>/<slug:name>/<int:marka_id>/', product_index, name="product_category"),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
from django.db.models.expressions import Exists
from django.shortcuts import render
from django.http import JsonResponse
from django.core import serializers
# from Filter.models import *
from .models import *
import json

# Create your views here.
def product_index(request,category,name,marka_id=None):
    subcat_id = SubCategory.objects.values('id','name').filter(main_category=category,id = name).last()
    product = Product.objects.filter(subcategory = subcat_id["id"])
    if marka_id != None:
        product = Product.objects.filter(subcategory = subcat_id["id"],marka = marka_id)
    else:
        product = Product.objects.filter(subcategory = subcat_id["id"]) 
    data = {
        'products': product,
        'markaes': Marka.objects.filter(main_category=category),
        'category': Filter.objects.all(),
        'link_category':category,
        'link_id':subcat_id['id'],
        'link_name':subcat_id['name'],
        'marka_id':marka_id
    }
    test = Product.objects.filter(id = 8).values('marka')
    return render(request,'product_index.html',data)

def get_product_ajax(request):
    id_list = request.GET.getlist('id[]')
    if request.GET.get("marka_id") != None:
        product = list(Product.objects.values('id','title','price','image','product_code').filter(category__in = id_list,marka = request.GET.get("marka_id")).distinct())    
    else:
        product = list(Product.objects.values('id','title','price','image','product_code').filter(category__in = id_list).distinct())
    data = {
        'product':product
    }
    return JsonResponse(data)
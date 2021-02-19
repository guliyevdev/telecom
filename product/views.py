from django.shortcuts import render
# from Filter.models import *
from .models import *

# Create your views here.
def product_index(request,category,name,filter_id=None):
    brend_id = SubCategory.objects.values('id','name').filter(main_category=category,id = name).last()
    if filter_id == None:
        product = Product.objects.filter(subcategory = brend_id["id"])
    else:
        product = Product.objects.filter(category = filter_id,subcategory = brend_id["id"]) 
    data = {
        'products': product,
        'subcats': SubCategory.objects.all(),
        'category': Filter.objects.all(),
        'link_category':category,
        'link_id':brend_id['id'],
        'link_name':brend_id['name']
    }
    return render(request,'product_index.html',data)
from django.shortcuts import render
# from Filter.models import *
from .models import *

# Create your views here.
def product_index(request,category,name,filter_id=None):
    brend_id = SubCategory.objects.values('id').filter(main_category=category,name = name).last()
    if filter_id == None:
        product = Product.objects.filter(subcategory = brend_id["id"])
    else:
        product = Product.objects.filter(category = filter_id,subcategory = brend_id["id"]) 
    data = {
        'products': product,
        'subcats': SubCategory.objects.all(),
        'category': Filter.objects.all(),
        'link_category':category,
        'link_name':name
    }
    return render(request,'product_index.html',data)
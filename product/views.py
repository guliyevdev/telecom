from django.shortcuts import render
# from Filter.models import *
from .models import *

# Create your views here.
def product_index(request,category,name,filter_id=None):
    brend_id = Brend.objects.values('id').filter(brend_category=category,name = name).last()
    if filter_id == None:
        product = Product.objects.filter(brend = brend_id["id"])
    else:
        product = Product.objects.filter(category = filter_id,brend = brend_id["id"]) 
    data = {
        'products': product,
        'brends': Brend.objects.all(),
        'category': Category.objects.all(),
        'link_category':category,
        'link_name':name
    }
    print(request)
    return render(request,'product_index.html',data)
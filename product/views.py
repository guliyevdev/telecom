from django.core import paginator
from django.db.models.expressions import Exists
from django.shortcuts import render
from django.http import JsonResponse
# from Filter.models import *
from .models import *
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

# Create your views here.
def product_index(request,category,name,marka_id=None):
    subcat_id = SubCategory.objects.values('id','name').filter(main_category=category,id = name).last()
    page = request.GET.get('page', 1)
    if marka_id != None:
        product_list = Product.objects.filter(subcategory = subcat_id["id"],marka = marka_id)
    else:
        product_list = Product.objects.filter(subcategory = subcat_id["id"])
    
    paginator = Paginator(product_list,15)
    
    try:
        product = paginator.page(page)
    except PageNotAnInteger:
        product = paginator.page(1)
    except EmptyPage:
        product = paginator.page(paginator.num_pages)
    
    data = {
        'products': product,
        'markaes': Marka.objects.filter(main_category=category),
        'category': Filter.objects.all(),
        'link_category':category,
        'link_id':subcat_id['id'],
        'link_name':subcat_id['name'],
        'marka_id':marka_id
    }
    return render(request,'product_index.html',data)

def get_product_ajax(request):
    id_list = request.GET.getlist('id[]')
    if request.GET.get("marka_id") != None:
        product_list = list(Product.objects.values('id','title','price','image','product_code').filter(category__in = id_list,marka = request.GET.get("marka_id")).distinct())    
    else:
        product_list = list(Product.objects.values('id','title','price','image','product_code').filter(category__in = id_list).distinct())
    
    data = {
        'product': product_list
    }
    return JsonResponse(data)
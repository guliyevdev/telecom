from product.views import product_index
from django.http import JsonResponse,HttpResponse
from django.shortcuts import render
from .models import *
from product.models import Product
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
# Create your views here.
# def links(request):
#     data = {
#         'links_telephones': Links.objects.all(),
#         'links_meiset': Links.objects.filter(category='Məişət texnikası')
#     }
#     return render(request,'index.html',data)


def post_create(request):
    if request.method == 'POST':
        if request.POST.get('email'):
            post = Email()
            post.email = request.POST.get('email')
            post.save()

            return render(request, 'index.html')

    else:
        return render(request, 'index.html')


def search_filter(request):
    product_data = list(Product.objects.values("title","image","price").filter(title__icontains = request.GET.get('input', None)))
    data = {
        "product_results" : product_data
        }
    return JsonResponse(data)
def search_results(request):
    page = request.GET.get('page', 1)
    search_value = request.GET.get('q', None)
    product_list = Product.objects.filter(title__icontains = search_value)
    paginator = Paginator(product_list,15)
    try:
        product = paginator.page(page)
    except PageNotAnInteger:
        product = paginator.page(1)
    except EmptyPage:
        product = paginator.page(paginator.num_pages)    
    data = {
        'products': product,
        'src_val': search_value
        }
    return render(request, 'product_search_results.html',data)

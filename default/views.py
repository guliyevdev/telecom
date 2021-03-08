from product.views import product_index
from django.http import JsonResponse,HttpResponse
from django.shortcuts import render
from .models import *
from product.models import Product
from django.core import serializers

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
    product_data = list(Product.objects.values("title","image"))
    data = {
        "product_results" : product_data
        }
    return JsonResponse(data)

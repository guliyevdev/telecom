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
    product = Product.objects.only('title').filter(title=request.POST.get("input")).last()
    if request.method == "POST":
    # data = {"name": "John", "age": 31, "city": "New York"}
        product = Product.objects.only('title').filter(title=request.POST.get("input"))
        product_data = serializers.serialize("json", Product.objects.only('title').filter(title=request.POST.get("input")))
        data = {"products" : product_data}
    else:
        data ={}
    # data = request
    return JsonResponse(data)

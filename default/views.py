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
    if request.method == "POST":
    # data = {"name": "John", "age": 31, "city": "New York"}
        # product_data = serializers.serialize("json", Product.objects.filter(title=request.POST.get("input")))
        product_data = Product.objects.values("title","image").filter(title=request.POST.get("input")).last()
        data = {"products" : product_data}
    else:
        data ={}
    # data = request
    product_data_one = Product.objects.values("id").filter(title=request.POST.get("input"))
    return JsonResponse(data)

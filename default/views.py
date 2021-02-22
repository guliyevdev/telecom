from product.views import product_index
from django.http import JsonResponse
from django.shortcuts import render
from .models import *

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
    # if request.method == "POST":
    # # data = {"name": "John", "age": 31, "city": "New York"}
    #     data = "OKEY"
    # else:
    #     data ="oppps"
    data = request
    return JsonResponse(data)

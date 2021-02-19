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
                post=Email()
                post.email= request.POST.get('email')
                post.save()
                
                return render(request, 'index.html')  

        else:
                return render(request,'index.html')


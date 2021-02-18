from .models import SubCategory

def links_renderer(request):
    return {
       'Kateqoriya1': SubCategory.objects.filter(main_category ='Kateqoriya1'),
       'Kateqoriya2': SubCategory.objects.filter(main_category ='Kateqoriya2'),
       'Kateqoriya3': SubCategory.objects.filter(main_category ='Kateqoriya3'),
       'Kateqoriya4': SubCategory.objects.filter(main_category ='Kateqoriya4'),
       'Kateqoriya5': SubCategory.objects.filter(main_category ='Kateqoriya5'),
       'Kateqoriya6': SubCategory.objects.filter(main_category ='Kateqoriya6'),
    }
from .models import SubCategory

def links_renderer(request):
    return {
       'Kateqoriya1': SubCategory.objects.filter(main_category ='Tikinti-materiallari'),
       'Kateqoriya2': SubCategory.objects.filter(main_category ='Pencere-ve-qapi'),
       'Kateqoriya3': SubCategory.objects.filter(main_category ='Isitme-ve-soyutma'),
       'Kateqoriya4': SubCategory.objects.filter(main_category ='Santexnika'),
       'Kateqoriya5': SubCategory.objects.filter(main_category ='Doseme-tavan-ve-dam'),
       'Kateqoriya6': SubCategory.objects.filter(main_category ='Temir-ve-tikinti-aletleri'),
    }
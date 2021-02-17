from .models import Brend

def links_renderer(request):
    return {
       'header_links_telephone': Brend.objects.filter(brend_category ='Telefon'),
       'header_links_kitchen': Brend.objects.filter(brend_category ='Məişət texnikası'),
       'header_links_tv': Brend.objects.filter(brend_category ='Tv auidio Foto və Əyləncə'),
       'header_links_computer': Brend.objects.filter(brend_category ='Kompüter Texnikasi'),
       'header_links_aksesuar': Brend.objects.filter(brend_category ='Aksesuarlar'),
       'header_links_outlet': Brend.objects.filter(brend_category ='Outlet'),
    }
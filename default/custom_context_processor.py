from .models import Contact

def contact_renderer(request):
   return {
      'contact': Contact.objects.all().last()
    }


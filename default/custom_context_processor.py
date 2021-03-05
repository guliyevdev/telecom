from .models import Contact,FourTitle

def contact_renderer(request):
   return {
      'contact': Contact.objects.all().last(),
      'fourtitle': FourTitle.objects.all().last()
    }


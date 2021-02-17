from django.db import models
from mptt.models import MPTTModel, TreeForeignKey,TreeManyToManyField
# Create your models here.

CATEGORY_CHOICES = (
    ('Telefon','Telefon,Planset'),
    ('Məişət texnikası', 'Məişət texnikası'),
    ('Tv auidio Foto və Əyləncə', 'Tv auidio Foto və Əyləncə'),
    ('Kompüter Texnikasi', 'Kompüter Texnikasi'),
    ('Aksesuarlar', 'Aksesuarlar'),
    ('Outlet', 'Outlet'),
)
class Category(MPTTModel):
    parent = TreeForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='children',verbose_name="Kateqoriya adı")
    subcat = models.CharField(max_length=50, unique=True)
    # slug = models.SlugField(unique=True,verbose_name="SLUG *bu hissə avtomatik doldurulur",blank=True,null=True)
    class MPTTMeta:
        order_insertion_by = ['subcat'] 
    def __str__(self):
        return self.subcat
        
    def has_children(self):
        return True if (self.get_children().count() > 0) else False
class Brend(models.Model):
    brend_category = models.CharField(max_length=200,choices=CATEGORY_CHOICES)
    name = models.CharField(max_length=200)       
    def __str__(self):
        return (self.name)

class Product(models.Model):
    brend = models.ForeignKey(Brend, on_delete=models.CASCADE)
    category = TreeManyToManyField('Category',null=True,blank=True)
    title = models.CharField(max_length=220)
    price = models.CharField(max_length=220)
    image = models.ImageField(null = False,blank =True, upload_to='static/images/product/')


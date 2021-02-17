from django.db import models
from mptt.models import MPTTModel, TreeForeignKey,TreeManyToManyField
from product.models import Category

# Create your models here.
CATEGORY_CHOICES = (
    ('Telefon','Telefon,Planset'),
    ('Məişət texnikası', 'Məişət texnikası'),
    ('Tv auidio Foto və Əyləncə', 'Tv auidio Foto və Əyləncə'),
    ('Kompüter Texnikasi', 'Kompüter Texnikasi'),
    ('Aksesuarlar', 'Aksesuarlar'),
    ('Outlet', 'Outlet'),
)
class Links(models.Model):
    list_category = models.CharField(max_length=200,choices=CATEGORY_CHOICES)
    name = models.CharField(max_length=220)
    slug = models.SlugField(max_length=200,unique=True)
from django.db import models
from mptt.models import MPTTModel, TreeForeignKey,TreeManyToManyField
# Create your models here.

CATEGORY_CHOICES = (
    ('Kateqoriya1','Kateqoriya1'),
    ('Kateqoriya2', 'Kateqoriya2'),
    ('Kateqoriya3', 'Kateqoriya3'),
    ('Kateqoriya4', 'Kateqoriya4'),
    ('Kateqoriya5', 'Kateqoriya5'),
    ('Kateqoriya6', 'Kateqoriya6'),
)
class Filter(MPTTModel):
    parent = TreeForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='children',verbose_name="Kateqoriya adı")
    subcat = models.CharField(max_length=50, unique=True)
    # slug = models.SlugField(unique=True,verbose_name="SLUG *bu hissə avtomatik doldurulur",blank=True,null=True)
    class MPTTMeta:
        order_insertion_by = ['subcat'] 
    def __str__(self):
        return self.subcat
        
    def has_children(self):
        return True if (self.get_children().count() > 0) else False
class SubCategory(models.Model):
    main_category = models.CharField(max_length=200,choices=CATEGORY_CHOICES)
    name = models.CharField(max_length=200)       
    def __str__(self):
        return (self.name)

class Product(models.Model):
    subcategory = models.ForeignKey(SubCategory, on_delete=models.CASCADE)
    category = TreeManyToManyField('Filter',null=True,blank=True)
    title = models.CharField(max_length=220)
    price = models.CharField(max_length=220)
    image = models.ImageField(null = False,blank =True, upload_to='static/images/product/')

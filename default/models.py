from django.db import models
from mptt.models import MPTTModel, TreeForeignKey,TreeManyToManyField
from product.models import Category

class Contact(models.Model):
    adress = models.CharField(max_length=220)
    number = models.CharField(max_length=220)
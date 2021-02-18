from django.db import models
from mptt.models import MPTTModel, TreeForeignKey,TreeManyToManyField
from product.models import Filter

class Contact(models.Model):
    adress = models.CharField(max_length=220)
    number = models.CharField(max_length=220)
    facebook = models.CharField(max_length=220,null=True,blank=True)
    instagram = models.CharField(max_length=220,null=True,blank=True)
    youtube = models.CharField(max_length=220,null=True,blank=True)
    whatsapp = models.CharField(max_length=220,null=True,blank=True)
from django.db import models

class Contact(models.Model):
    adress = models.CharField(max_length=220)
    number = models.CharField(max_length=220)
    facebook = models.CharField(max_length=220,null=True,blank=True)
    instagram = models.CharField(max_length=220,null=True,blank=True)
    youtube = models.CharField(max_length=220,null=True,blank=True)
    whatsapp = models.CharField(max_length=220,null=True,blank=True)

class Email(models.Model):
    email = models.CharField(max_length=220)

class FourTitle(models.Model):
    titleone = models.CharField(max_length=220,verbose_name="Başlıq Bir",null=True)
    titletwo = models.CharField(max_length=220,verbose_name="Başlıq İki",null=True)
    titlethree = models.CharField(max_length=220,verbose_name="Başlıq Üç",null=True)
    titlefour = models.CharField(max_length=220,verbose_name="Başlıq Dörd",null=True)
    class Meta:
        verbose_name = '4 Başlıq'
        verbose_name_plural = '4 Başlıq'
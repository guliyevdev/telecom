from django.db import models

# Create your models here.
 
class Slider(models.Model):
    title = models.CharField(max_length=220,null=True,blank=True)
    image = models.ImageField(upload_to='static/images/home/')
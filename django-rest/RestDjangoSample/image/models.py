from django.db import models

# Create your models here.
class Image(models.Model):
    imageFile = models.ImageField(default = 'no-img.png', max_length=254, blank=True, null=True)  #upload_to = 'media/',   

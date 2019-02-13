from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=64)
    author = models.CharField(max_length=20)
    publisher = models.CharField(max_length=20)
    rentalStatus = models.IntegerField
    summary = models.CharField(max_length=200)
    releaseDate = models.DateField
    category = models.CharField(max_length=20)
    pub_date = models.DateTimeField('date published')
    def __str__(self):
        return self.title
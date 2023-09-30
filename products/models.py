from django.db import models

# Create your models here.
class product(models.Model):
   name = models.CharField(max_length=100)
   price = models.FloatField()
   stock = models.IntegerField()
   image = models.CharField(max_length=2500)

class offers(models.Model):
   code = models.CharField(max_length=16)
   discription = models.CharField(max_length=255)
   discount = models.FloatField()

class emplo(models.Model):
   name = models.CharField(max_length=30)
   place = models.CharField(max_length=100)
   age = models.IntegerField()   
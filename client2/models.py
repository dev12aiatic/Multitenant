from django.db import models

# Create your models here.
class Product2(models.Model):
  name= models.CharField(max_length=100)
  description= models.TextField()
  stock = models.IntegerField()
  def __str__(self):
    return self.name
    
class Category2(models.Model):
  name= models.CharField(max_length=100)
  description= models.TextField()
  def __str__(self):
    return self.name

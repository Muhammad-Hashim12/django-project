from django.db import models

# Create your models here.

class Packages(models.Model):
    name= models.CharField(max_length=50)
    img= models.ImageField(upload_to='pics')
    days= models.TextField()
    person= models.TextField()
    price= models.IntegerField()
    desc= models.TextField()



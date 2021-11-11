from django.db import models

# Create your models here.
class contacts(models.Model):
    name=models.CharField(max_length=20)
    email=models.EmailField()
    phNo=models.CharField(max_length=12)

class services(models.Model):
    pic=models.ImageField(upload_to='pics')
    heading=models.CharField(max_length=30)
    descr=models.TextField()
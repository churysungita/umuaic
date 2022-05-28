from email.mime import image
from turtle import title
from django.db import models

# Create your models here.
class gallery(models.Model):
    imageCaption=models.TextField(max_length=50)
    imageGallery=models.ImageField(upload_to='media/')
    
    def __str__(self):
        return self.imageCaption
    
class projects(models.Model):
    title=models.CharField(max_length=50)
    description=models.TextField(max_length=100)
    image=models.ImageField(upload_to='media/')
    
    def __str__(self):
        return self.title

class activities(models.Model):
    title=models.CharField(max_length=300)
    description=models.TextField(max_length=1000)
    image=models.ImageField(upload_to='media/')
    kiasi_kilichopatikana=models.CharField(max_length=50)
    kiasi_kinachohitajika=models.CharField(max_length=50)
    
    def __str__(self):
        return self.title
    
  
    
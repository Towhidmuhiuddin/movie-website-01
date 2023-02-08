from django.db import models

from datetime import datetime,date


import os

def get_file_path(request,filename):
    original_filename = filename
    nowTime=datetime.datetime.now().strftime('%Y%M%D%H:%M:%S')
    filename="%s%s" % (nowTime,original_filename)
    return os.path.join('uploads/', filename)
# Create your models here.
class Category(models.Model):
    slug=models.CharField(max_length=150,null=False,blank=False)
    name=models.CharField(max_length=150,null=False,blank=False)
    image=models.ImageField(upload_to=get_file_path,null=True,blank=True)
    description=models.TextField(max_length=500,null=False,blank=False)
    status=models.BooleanField(default=False,help_text="0=default,1=hidden")
    release=models.BooleanField(default=False,help_text="0=default,1=Release")
    created_at=models.DateTimeField( auto_now_add=True)

    def __str__(self):
        return self.name
    
class Movie(models.Model):
    category=models.ForeignKey(Category,on_delete=models.CASCADE)
    slug=models.CharField(max_length=150,null=False,blank=False)
    name=models.CharField(max_length=150,null=False,blank=False)
    movie_image=models.ImageField(upload_to=get_file_path,null=True,blank=True)
    producer=models.CharField(max_length=150,null=False,blank=False)
    actor=models.CharField(max_length=500, null=False, blank=False)
    small_description=models.CharField(max_length=500,null=False,blank=False)
    quantity=models.IntegerField(null=False,blank=False)
    description=models.TextField(max_length=500,null=False,blank=False)
    original_price=models.FloatField(null=False,blank=False)
    selling_price=models.FloatField(null=False,blank=False)
    scedule_date=models.DateField(auto_now=False, auto_now_add=False,blank=True)
    status=models.BooleanField(default=False,help_text="0=default,1=hidden")
    release=models.BooleanField(default=False,help_text="0=default,1=Release")
    tag=models.CharField(max_length=150,null=False,blank=False)
    created_at=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
    
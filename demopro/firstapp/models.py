from django.db import models
#import it
from django.db import connection

#after from views.py then Create your models here. 
class Contact(models.Model):
    name=models.CharField( max_length=50)
    email=models.CharField( max_length=50)
    password=models.CharField( max_length=50)
class Signupdata(models.Model):
    name=models.CharField( max_length=50)
    email=models.CharField( max_length=50)
    gender=models.CharField( max_length=50)
    date=models.CharField(max_length=50)

    #after all these we must register in admin.py

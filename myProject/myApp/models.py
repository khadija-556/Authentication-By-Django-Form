from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class Custom_user(AbstractUser):
    USER =[
        ('jobseeker','JobSeeker'),
        ('recuiter','Recuiter')
    ]
    
    city=models.CharField(max_length=100,null=True)
    user_type=models.CharField(choices=USER,max_length=100)
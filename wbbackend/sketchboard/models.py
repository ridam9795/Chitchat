from django.db import models
from django.contrib.auth.models import AbstractUser
from .manager import UserManager
from django.contrib.postgres.fields import ArrayField

# Create your models here.

class User(AbstractUser):
    username = models.CharField(max_length=40, unique=False, default='',blank=True)
    phone_number=models.CharField(max_length=10,unique=True)
    is_phone_verified=models.BooleanField(default=False)
    otp=models.CharField(max_length=6)
    
    USERNAME_FIELD='phone_number'
    REQUIRED_FIELDS=[]
    objects=UserManager()
    
    
class Contact(models.Model):
    phone_number=models.CharField(max_length=10,default='',blank=True)
    user=models.ForeignKey('User',on_delete=models.CASCADE,null=True,blank=True)
    
    def __str__(self) -> str:
        return self.name
    
   
    
    
    
class Chat(models.Model):
    content=models.CharField(max_length=1000)
    timestamp=models.DateTimeField(auto_now=True) 
    group=models.ForeignKey('Group',on_delete=models.CASCADE)  
    
    
class Group(models.Model):
    name=models.CharField(max_length=250)
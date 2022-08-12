from unicodedata import name
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models.signals import post_save
from django.dispatch import receiver


class CustomUser(AbstractUser):
    user_type_data=((1,"Admin"),(2,"Staff"),(3,"Student"))
    user_type=models.CharField(default=1,choices=user_type_data,max_length=10)

class Request(models.Model):
    id = models.AutoField(primary_key=True)
    purpose = models.CharField(max_length=200)
    status = models.CharField(max_length=20)
    sender = models.ForeignKey(CustomUser,related_name='user_sender',on_delete=models.CASCADE)
    receiver = models.ForeignKey(CustomUser,related_name='user_receiver',on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)
    objects=models.Manager()

class Recommendation_letter(models.Model):
    id = models.AutoField(primary_key=True)
    request = models.OneToOneField(Request,on_delete=models.CASCADE)
    text = models.CharField(max_length=300)
    timestamp = models.DateTimeField(auto_now_add=True)
    objects=models.Manager()

class Lesson(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)
    grade = models.CharField(max_length=200)
    request = models.ForeignKey(Request,on_delete=models.CASCADE)
    semester = models.CharField(max_length=200)
    objects=models.Manager()



import datetime
from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone   
import os


class Mesaj(models.Model):
    msg_text = models.CharField(max_length=255)
    pub_date = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    msg_image = models.ImageField(null=True,blank=True, upload_to="photo/")
        
    class Meta:
        ordering = ('pub_date',)

from jsonfield import JSONField
from django.db import models
from django.contrib.auth.models import User
#from django.db.models.signals import post_save
from django.dispatch import receiver
#from django_pg import models
import requests, json
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField
    

class Room(models.Model):
    title = models.CharField(max_length=45)
    zoom_url = models.CharField(max_length = 1000)
    meeting_id = models.CharField(max_length = 100)
    course = models.CharField(max_length = 100)
    notes = RichTextUploadingField(blank = True)
    #course = models.ArrayField(models.CharField(max_length = 100))
    #Users = ArrayField(models.CharField(max_length=200), blank=True)
    #Users = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

class Profile(models.Model):
    #name = models.CharField(max_length=60)
    #image_url = models.CharField(max_length=1000)
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    zoom_id = models.CharField(max_length = 100)
    section = models.CharField(max_length = 100)
    image = models.ImageField(upload_to = "images/", default="")
    first_login = models.BooleanField()
    classes = JSONField()

class Section(models.Model):
    name = models.CharField(max_length = 1000)
    isSection = models.BooleanField()

    def __str__(self):
        return self.name


class Token(models.Model):
    access_token = models.TextField()
    refresh_token = models.TextField()
# Create your models here.


from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

class Room(models.Model):
    title = models.CharField(max_length=33)
    #Users = ArrayField(models.CharField(max_length=200), blank=True)
    #Users = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

class Profile(models.Model):
    name = models.CharField(max_length=60)
    image_url = models.CharField(max_length=1000)
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    user = models.OneToOneField(User, on_delete=models.CASCADE)

# Create your models here.

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance, room = Room.objects.get(title = "inactive") )
        

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()
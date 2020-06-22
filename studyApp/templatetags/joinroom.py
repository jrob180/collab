from django import template
from django.template.defaultfilters import stringfilter
from django.shortcuts import redirect
from ..models import User, Room

register = template.Library()

@register.filter(name = "joinroom")
def joinroom(room_title):
    user = User.objects.get(name = "Arul Kapoor")
    user.room = Room.objects.get(title = room_title) 
    user.save()
    return ''
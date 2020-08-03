from django import forms
from .models import Profile


class NameForm(forms.Form):
    your_name = forms.CharField(max_length=33, label = '')

class ImageForm(forms.Form):
    image = forms.ImageField()
    #class Meta: 
    #        model = Profile
    #        fields = ['image'] 
    #class Meta: 
    #    model = Profile 
    #    fields = ['img_url'] 

    
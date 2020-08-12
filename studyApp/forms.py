from django import forms
from .models import Profile, Section


class NameForm(forms.Form):
    your_name = forms.CharField(max_length=33, label = '')

class ImageForm(forms.Form):
    image = forms.ImageField()



class SectionForm(forms.Form):


    # sections = list(Section.objects.all().values_list('name', flat=True))
    # SECTION_CHOICES = []
    # for i in range(len(sections)):
    #     SECTION_CHOICES.append((sections[i], sections[i]))

    # section = forms.CharField(label='What section are you in?', 
    # widget=forms.Select(choices=SECTION_CHOICES))

    section = forms.ModelChoiceField(queryset = Section.objects.all(), to_field_name="name", empty_label=None, label = "What section are you in?",
    widget=forms.Select(attrs={'class':'choices-page', 'id': 'choices-page-modal'}))

    
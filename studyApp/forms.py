from django import forms
from .models import Profile, Section, Room
from django.forms import ModelForm
from datetime import datetime
from dateutil import tz

def classset():
    classlist = list(Section.objects.order_by('name').values_list('name', flat = True))
    class_tuple = []
    for i in range(len(classlist)):
        class_tuple.append((classlist[i],classlist[i]))
    return class_tuple


def get_time():
    now = datetime.now()
    utc = now.replace(tzinfo = tz.tzutc())
    local = utc.astimezone(tz.tzlocal())
    #timezonenow = now.replace(tzinfo=timezone.utc).astimezone(tz=None)
    return local.strftime('%m/%d/%Y %H:%M')

class NameForm(forms.Form):
    your_name = forms.CharField(max_length=40, label = '' )
    isSchedule = forms.BooleanField(initial=False, label = 'Schedule for now or later?', required=False, 
        widget=forms.CheckboxInput(attrs={
                'class': 'checkmark'
            })
        )
    # widget=forms.Boolean(attrs={'class':'check', 'id': 'check'}))
    date = forms.DateTimeField(
        input_formats=['%m/%d/%Y %H:%M'], initial=get_time,
        widget=forms.DateTimeInput(attrs={
            'class': 'form-control datetimepicker-input',
            'data-target': '#datetimepicker1'
        })
    )


class ImageForm(forms.Form):
    image = forms.ImageField()

class TextForm(forms.ModelForm):
    class Meta:
        model = Room
        fields = ['notes']


class SectionForm(forms.Form):


    # sections = list(Section.objects.all().values_list('name', flat=True))
    # SECTION_CHOICES = []
    # for i in range(len(sections)):
    #     SECTION_CHOICES.append((sections[i], sections[i]))

    # section = forms.CharField(label='What section are you in?', 
    # widget=forms.Select(choices=SECTION_CHOICES))

    #section = forms.ModelChoiceField(queryset = Section.objects.all(), to_field_name="name", empty_label=None, label = "What section are you in?",
    #widget=forms.Select(attrs={'class':'choices-page', 'id': 'choices-page-modal'}))
    #class0 = forms.ModelChoiceField(queryset = Section.objects.filter(name = test), to_field_name="name", empty_label=None, label = "What is your first class?",
    #widget=forms.Select(attrs={'class':'choices-page', 'id': 'choices-page-modal'}))
    class1 = forms.ModelChoiceField(queryset = Section.objects.filter(isSection = False), to_field_name="name", empty_label=None, label = "Thread 1",
    widget=forms.Select(attrs={'class':'choices-page', 'id': 'choices-page-modal'}))
    class2 = forms.ModelChoiceField(queryset = Section.objects.filter(isSection = False), to_field_name="name", empty_label=None, label = "Thread 2",
    widget=forms.Select(attrs={'class':'choices-page', 'id': 'choices-page-modal'}))
    class3 = forms.ModelChoiceField(queryset = Section.objects.filter(isSection = False), to_field_name="name", empty_label=None, label = "Thread 3",
    widget=forms.Select(attrs={'class':'choices-page', 'id': 'choices-page-modal'}))
    class4 = forms.ModelChoiceField(queryset = Section.objects.filter(isSection = False), to_field_name="name", empty_label=None, label = "Thread 4",
    widget=forms.Select(attrs={'class':'choices-page', 'id': 'choices-page-modal'}))
    class5 = forms.ModelChoiceField(queryset = Section.objects.filter(isSection = False), to_field_name="name", empty_label=None, label = "Thread 5",
    widget=forms.Select(attrs={'class':'choices-page', 'id': 'choices-page-modal'}))

    
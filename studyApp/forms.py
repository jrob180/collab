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
    your_name = forms.CharField(max_length=33, label = '')
    # isSchedule = forms.BooleanField(initial=False, label = 'Schedule for now or later?', required=False)
    # date = forms.DateTimeField(
    #     input_formats=['%m/%d/%Y %H:%M'], initial=get_time,
    #     widget=forms.DateTimeInput(attrs={
    #         'class': 'form-control datetimepicker-input',
    #         'data-target': '#datetimepicker1'
    #     })
    # )


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

    def __init__(self, *args, **kwargs):
        super(SectionForm, self).__init__(*args, **kwargs)
        classlist = list(Section.objects.order_by('name').values_list('name', flat = True))
        self.class_tuple = []
        for i in range(len(classlist)):
            self.class_tuple.append((classlist[i],classlist[i]))


        self.fields['class1'] = forms.ChoiceField(choices = self.class_tuple, label = "What is your first thread?",
        widget=forms.Select(attrs={'class':'choices-page', 'id': 'choices-page-modal'}))
        self.fields['class2'] = forms.ChoiceField(choices = self.class_tuple, label = "What is your second thread?",
        widget=forms.Select(attrs={'class':'choices-page', 'id': 'choices-page-modal'}))
        self.fields['class3'] = forms.ChoiceField(choices = self.class_tuple, label = "What is your third thread?",
        widget=forms.Select(attrs={'class':'choices-page', 'id': 'choices-page-modal'}))
        self.fields['class4'] = forms.ChoiceField(choices = self.class_tuple, label = "What is your fourth thread?",
        widget=forms.Select(attrs={'class':'choices-page', 'id': 'choices-page-modal'}))
        self.fields['class5'] = forms.ChoiceField(choices = self.class_tuple, label = "What is your fifth thread?",
        widget=forms.Select(attrs={'class':'choices-page', 'id': 'choices-page-modal'}))


    
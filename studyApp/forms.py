from django import forms
from .models import Profile, Section, Room
from django.forms import ModelForm

classlist = list(Section.objects.order_by('name').values_list('name', flat = True))
classset = []
for i in range(len(classlist)):
    classset.append((classlist[i],classlist[i]))


    
class NameForm(forms.Form):
    your_name = forms.CharField(max_length=33, label = '')
    # isSchedule = forms.BooleanField(initial=False, label = 'Schedule for now or later?', required=False)
    # time = forms.TimeField(required = False, widget=forms.TimeInput(format='%H:%M'))

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
    # classset = Section.objects.filter(name = "----").values_list('name', flat = True)
    # classset = [("----","----")]
    # class1 = forms.ModelChoiceField(queryset = classset, empty_label=None, label = "What is your first class?",
    # widget=forms.Select(attrs={'class':'choices-page', 'id': 'choices-page-modal'}))
    # class2 = forms.ModelChoiceField(queryset = classset, to_field_name="name", empty_label=None, label = "What is your second class?",
    # widget=forms.Select(attrs={'class':'choices-page', 'id': 'choices-page-modal'}))
    # class3 = forms.ModelChoiceField(queryset = classset, to_field_name="name", empty_label=None, label = "What is your third class?",
    # widget=forms.Select(attrs={'class':'choices-page', 'id': 'choices-page-modal'}))
    # class4 = forms.ModelChoiceField(queryset = classset, to_field_name="name", empty_label=None, label = "What is your fourth class?",
    # widget=forms.Select(attrs={'class':'choices-page', 'id': 'choices-page-modal'}))
    # class5 = forms.ModelChoiceField(queryset = classset, to_field_name="name", empty_label=None, label = "What is your fifth class?",
    # widget=forms.Select(attrs={'class':'choices-page', 'id': 'choices-page-modal'}))

    # class1 = forms.ModelChoiceField(queryset = classset, empty_label=None, label = "What is your first class?",
    # widget=forms.Select(attrs={'class':'choices-page', 'id': 'choices-page-modal'}))
    # class2 = forms.ModelChoiceField(queryset = classset, empty_label=None, label = "What is your second class?",
    # widget=forms.Select(attrs={'class':'choices-page', 'id': 'choices-page-modal'}))
    # class3 = forms.ModelChoiceField(queryset = classset, empty_label=None, label = "What is your third class?",
    # widget=forms.Select(attrs={'class':'choices-page', 'id': 'choices-page-modal'}))
    # class4 = forms.ModelChoiceField(queryset = classset, empty_label=None, label = "What is your fourth class?",
    # widget=forms.Select(attrs={'class':'choices-page', 'id': 'choices-page-modal'}))
    # class5 = forms.ModelChoiceField(queryset = classset, empty_label=None, label = "What is your fifth class?",
    # widget=forms.Select(attrs={'class':'choices-page', 'id': 'choices-page-modal'}))


    class1 = forms.ChoiceField(choices = classset, label = "What is your first class?",
    widget=forms.Select(attrs={'class':'choices-page', 'id': 'choices-page-modal'}))
    class2 = forms.ChoiceField(choices = classset, label = "What is your second class?",
    widget=forms.Select(attrs={'class':'choices-page', 'id': 'choices-page-modal'}))
    class3 = forms.ChoiceField(choices = classset, label = "What is your third class?",
    widget=forms.Select(attrs={'class':'choices-page', 'id': 'choices-page-modal'}))
    class4 = forms.ChoiceField(choices = classset, label = "What is your fourth class?",
    widget=forms.Select(attrs={'class':'choices-page', 'id': 'choices-page-modal'}))
    class5 = forms.ChoiceField(choices = classset, label = "What is your fifth class?",
    widget=forms.Select(attrs={'class':'choices-page', 'id': 'choices-page-modal'}))


    
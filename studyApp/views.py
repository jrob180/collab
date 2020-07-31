from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Room
from .models import Profile
from django.views.generic import CreateView
from .forms import NameForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.contrib.auth.models import User
from django.template.context_processors import csrf

class Counter:
    count = 0

    def increment(self):
        self.count += 1
        return ''

    def zero(self):
        self.count = 0
        return ''

# Create your views here.


@login_required(login_url='login/')
def home(request):

    if request.method == 'POST':
        form = NameForm(request.POST)
        if form.is_valid():
            text = form.cleaned_data['your_name']
            room = Room()
            room.title = text 
            room.save()

            user = Profile.objects.get(user = request.user)
            user.room = room
            user.save()

            form = NameForm()
            return redirect('studyApp-home')

    c = Counter()

    form = NameForm()

    context = {
        'rooms': Room.objects.all(),
        'users': Profile.objects.all(),
        'counter': c,
        'form': form,
    }
    return render(request, 'studyApp/index.html', context)

def login(request):
    return render(request, 'studyApp/login.html')

def logout(request):
    logout(request)
    return render('studyApp/index.html')

def joinroom(request):
    if request.method == 'GET':
        room = request.GET['room_id']
        user = Profile.objects.get(user = request.user)
        user.room = Room.objects.get(title = room) 
        user.save()
        return HttpResponse("success")
    else:
        return HttpResponse("Request method is not a GET")
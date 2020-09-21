from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Room
from .models import Profile, Section, Token
from django.views.generic import CreateView
from .forms import NameForm, ImageForm, SectionForm, TextForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.contrib.auth.models import User
import json
import requests
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST
from django.db.models.signals import post_save
from django.dispatch import receiver
import base64
import time
from django.db.models import Q
# from selenium import webdriver
# from selenium.webdriver.common.by import By

# from selenium.common.exceptions import TimeoutException

# from selenium.webdriver.support.ui import WebDriverWait # available since 2.4.0

# from selenium.webdriver.support import expected_conditions as EC # available since 2.26.0
# from bs4 import BeautifulSoup


#import pandas as pd
#from django.contrib.staticfiles.storage import staticfiles_storage




#token = 'eyJhbGciOiJIUzUxMiIsInYiOiIyLjAiLCJraWQiOiIyNWYyMjA2YS1lODA3LTRlMjUtYjhjYi0wZGZjMjBhYjdiNWIifQ.eyJ2ZXIiOiI2IiwiY2xpZW50SWQiOiJ6SmliOG5Rc1RHMFFBX0pnRXFqNVEiLCJjb2RlIjoiZXVnNWlrSG9LZF95ZWlWdUlXc1FfNjNOOUtEY3F1aG9nIiwiaXNzIjoidXJuOnpvb206Y29ubmVjdDpjbGllbnRpZDp6SmliOG5Rc1RHMFFBX0pnRXFqNVEiLCJhdXRoZW50aWNhdGlvbklkIjoiMjM2NDJlMTFlYjBiZTFhZGNiMmFkYjZjNTFhOWJlNDkiLCJ1c2VySWQiOiJ5ZWlWdUlXc1FfNjNOOUtEY3F1aG9nIiwiZ3JvdXBOdW1iZXIiOjAsImF1ZCI6Imh0dHBzOi8vb2F1dGguem9vbS51cyIsImFjY291bnRJZCI6ImhORE8zbG1NU3RTNnhjcS1iMy1QMUEiLCJuYmYiOjE1OTQ0Mzc2NzQsImV4cCI6MTU5NDQ0MTI3NCwidG9rZW5UeXBlIjoiYWNjZXNzX3Rva2VuIiwiaWF0IjoxNTk0NDM3Njc0LCJqdGkiOiJiYWQxNjhjOS03YTc3LTRlYTMtOGI2OC1mZWUwMGIzNWE1ODkiLCJ0b2xlcmFuY2VJZCI6MjJ9.ztaR-aKWc0tiPkmbtwlYQUO92cwURNbXRQxNt_75uvex0rIlTVpQJajgj_TNx5uFheHLfcnCT0-0E13gRgXOHw'
start = 4000
def read_file(request):
    f = open('/Users/arulkapoor118/collab_website/collab/studyApp/loaderio-4049d7ee993d07bdda5b43856ece8ea9.txt', 'r')
    file_content = f.read()
    f.close()

    # Create a new instance of the Firefox driver
    # driver = webdriver.Chrome('/Users/arulkapoor118/Downloads/chromedriver')

    # # go to the google home page
    # url = "http://bulletin.columbia.edu/columbia-college/departments-instruction/search/?term=3&pl=0&ph=10&college=CC"

    # driver.get(url)
    # try:    
    #     WebDriverWait(driver, 22).until(
    #         EC.visibility_of_element_located((By.CLASS_NAME, 'courseblocktitle'))
    #     )
        
    #     #a = element.text
    #     a=driver.page_source

    # finally:
    #     driver.quit()

    # page_soup = BeautifulSoup(a, 'html.parser')
    # results = page_soup.find(id='scopo-results')
    # job_elems = results.find_all('p', class_='courseblocktitle')

    # courses = []
    # for job_elem in job_elems:
    #     courses.append(job_elem.text.split('.  ')[0].replace(u'\xa0', u' '))
    # catalog_numbers=[]
    # for i in range(len(courses)):
    #     catalog_numbers.append(courses[i].split(' ',2)[0] + ' ' + courses[i].split(' ',2)[2])
    # filename = "static/princeton2.csv"
    # filename = staticfiles_storage.path('princeton2.csv')

    # column = "catalog-number"
    # school = "princeton"

    # df = pd.read_csv(filename)
    # catalog_numbers = df[column].tolist()

    #Remove when we can organize classes by course name and id 
    # (can probably do that with a model update)
    catalog_numbers = list(set(catalog_numbers))

    for c in catalog_numbers:
        course = Section(name = c, isSection = False, school = 'columbia')
        course.save()
    return HttpResponse(file_content, content_type="text/plain")

class Counter:
    count = 0

    def increment(self):
        self.count += 1
        return ''

    def zero(self):
        self.count = 0
        return ''

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        '''
        global start
        start+=1
        
        headers = {'Authorization': "Bearer " + token, 'host': 'zoom.us', "Content-Type": 'application/json'}
        payload = {
        "action": "custCreate",
        "user_info": {
            "email": str(start)+'l'+'@sdf.gh',
            "type": 1,
            "first_name": str(instance.first_name),
            "last_name": str(instance.last_name)
        }
        }
        user_endpoint = 'https://api.zoom.us/v2/users'
        u = requests.post(user_endpoint, headers = headers, json = payload)
        id = json.loads(u.text)['id']
        Profile.objects.create(user=instance, room = Room.objects.get(title = "inactive"), zoom_id= id)
        '''
        image = None
        email = instance.email
        school = email.split('@')[1]
        if school == 'college.harvard.edu':
            school = "harvard"
        elif school == 'princeton.edu':
            school = "princeton"
        elif school == 'stanford.edu':
            school = "stanford"
        elif school == 'penn.edu':
            school = "upenn"
        elif school == 'columbia.edu':
            school = "columbia"
        # course = ...
        Profile.objects.create(user=instance, room = Room.objects.get(title = "inactive"), zoom_id= "", section = "", image = image, first_login = True, classes = {}, school = school)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()

@csrf_exempt
@require_POST
def meetingend(request):
    jsondata = request.body
    data = json.loads(jsondata)
    #meetingtopic = data['payload']['object']['topic']
    #room = Room.objects.get(title = meetingtopic)
    meetingid = data['payload']['object']['id']
    room = Room.objects.get(meeting_id = meetingid)

    inactive = Room.objects.get(title = "inactive")

    Profile.objects.filter(room = room).update(room=inactive)
    room.delete()

    return HttpResponse(status=200)


'''
@csrf_exempt
@require_POST
def meetingstart(request):
    jsondata = request.body
    data = json.loads(jsondata)
    #meetingtopic = data['payload']['object']['topic']
    #room = Room.objects.get(title = meetingtopic)
    meetingid = data['payload']['object']['topic']
    room = Room.objects.get(meeting_id = meetingid)

    inactive = Room.objects.get(title = "inactive")

    Profile.objects.filter(room = room).update(room=inactive)
    room.delete()

    return HttpResponse(status=200)
'''

@csrf_exempt
@require_POST
def participantleft(request):
    jsondata = request.body
    data = json.loads(jsondata)
    inactive = Room.objects.get(title = "inactive")
    
    print(data['payload']['object']['participant'])

    zoom_id = data['payload']['object']['participant']['user_name']
    meeting_id = data['payload']['object']['id']

    if Room.objects.filter(meeting_id = meeting_id).exists():
        room = Room.objects.get(meeting_id = meeting_id)

        if Profile.objects.filter(user__username = zoom_id, room = room).exists():
            Profile.objects.filter(user__username = zoom_id, room = room).update(room = inactive)
    
    return HttpResponse(status=200)

'''@csrf_exempt
@require_POST
def participantjoin(request):
    jsondata = request.body
    data = json.loads(jsondata)
    meeting_id = data['payload']['object']['id']
    #participants = get_participants(token, meeting_id)
    room = Room.objects.get(meeting_id = meeting_id)
    if Profile.objects.filter(room = room, zoom_id = "").exists():
        user = Profile.objects.get(room = room, zoom_id = "")
        user.zoom_id = data['payload']['object']['participant']['id']
        user.save()
    #for p in participants:
    #    if not Profile.objects.filter(zoom_id = p['id'])
    #        user.zoom_id = p['id']
    #meta = copy.copy(request.META)
    
    return HttpResponse(status=200)
'''
# Create your views here.
def uploadImage(request):
    if request.method == 'POST':
        form = ImageForm(request.POST, request.FILES)
        
        if form.is_valid(): 
            profile = request.user.profile
            profile.image = form.cleaned_data['image']
            profile.save()
        return redirect('studyApp-home')


def createroom(request):
    if request.method == 'GET':
        title = request.GET['room_title']
        course_ind = request.GET['course']

        form = NameForm()
        global start
        user = Profile.objects.get(user = request.user)
        print(course_ind)
        course = user.classes['classes'][int(course_ind)]
        #rooms = start_meeting(token, start, title, user.zoom_id)
        
        refresh_access_token()

        token = Token.objects.get(id = 1).access_token
        rooms = start_meeting(token, start, title, request.user.first_name, request.user.last_name)
        #rooms = ['hi', 'hi','hi']

        room = Room()
        room.title = title
        room.zoom_url = rooms[1]
        room.meeting_id = rooms[2]
        room.course = course
        room.save()
        
        user.room = room
        user.save()

        start+=1
        data = {
            'meeting': rooms[0]
        }
        return JsonResponse(data)
    else:
        return HttpResponse("Request method is not a GET")


@login_required(login_url='login/')
def home(request):
    if request.user.profile.first_login:
        return redirect('studyApp-classes')

    course = request.path[1:-1]
    user = request.user
   
    
    # elif course == 'section':
    #     #course = 'SECTION ABC'
    #     course = user.profile.section
    rooms = 0
    classes = user.profile.classes
    for i in range(1,6):
        if course == "class{i}".format(i=i):
            course = classes['classes'][i-1]
            rooms = Room.objects.filter(course = course)

    
    if course == "":
        course = classes['classes']
        rooms = Room.objects.filter(course__in = course)
        course = ""

    if user.username != user.get_full_name and user.username != 'arulkapoor118':
        user.username = str(user.get_full_name())
        user.save()
        
    c = Counter()

    form = NameForm()
    img_form = ImageForm()
    section_form = SectionForm()
    text_form = TextForm()

    
    context = {
        #'rooms': Room.objects.all(),
        'rooms': rooms,
        'users': Profile.objects.all(),
        'counter': c,
        'classes': classes['classes'],
        'course': course,
        'form': form,
        'img_form': img_form,
        'section_form': section_form,
        'text_form': text_form
    }
    return render(request, 'studyApp/index.html', context)

@login_required(login_url='login/')
def classes(request):
    # if not request.user.profile.first_login:
    #     return redirect('studyApp-home')

    form = SectionForm()
    form.fields['class1'].queryset = Section.objects.filter(Q(school = request.user.profile.school) | Q(name = "----")).order_by('name')
    form.fields['class2'].queryset = Section.objects.filter(Q(school = request.user.profile.school) | Q(name = "----")).order_by('name')
    form.fields['class3'].queryset = Section.objects.filter(Q(school = request.user.profile.school) | Q(name = "----")).order_by('name')
    form.fields['class4'].queryset = Section.objects.filter(Q(school = request.user.profile.school) | Q(name = "----")).order_by('name')
    form.fields['class5'].queryset = Section.objects.filter(Q(school = request.user.profile.school) | Q(name = "----")).order_by('name')
    context = {
        #'rooms': Room.objects.all(),
        'form': form,

    }
    return render(request, 'studyApp/classes.html', context)

def selectClass(request):
    if request.method == 'POST':
        form = SectionForm(request.POST)
    
        if form.is_valid(): 
            profile = request.user.profile
            #profile.section = form.cleaned_data['section'].name.upper()

            class1 = form.cleaned_data['class1'].name.upper()
            class2 = form.cleaned_data['class2'].name.upper()
            class3 = form.cleaned_data['class3'].name.upper()
            class4 = form.cleaned_data['class4'].name.upper()
            class5 = form.cleaned_data['class5'].name.upper()

            classes = list(set([class1, class2, class3, class4, class5]))
            profile.classes = {'classes':classes}
            profile.first_login = False
            profile.save()
        return redirect('studyApp-home')

def login(request):
    return render(request, 'studyApp/login.html')


def joinroom(request):
    if request.method == 'GET':
        room = request.GET['room_id']
        user = Profile.objects.get(user = request.user)

        user.room = Room.objects.get(meeting_id = room) 
        user.save()
        #zoom api call to get all meeting participants, and then loop over participant ids and check 
        return HttpResponse("success")
    else:
        return HttpResponse("Request method is not a GET")

def start_meeting(access_token, index, topic, firstname, lastname):
    global start
    start+=1
    
    headers = {'Authorization': "Bearer " + access_token, 'host': 'zoom.us', "Content-Type": 'application/json'}
    payload = {
    "action": "custCreate",
    "user_info": {
        "email": str(start)+'l'+'@sdf.gh',
        "type": 1,
        "first_name": firstname,
        "last_name": lastname
    }
    }
    user_endpoint = 'https://api.zoom.us/v2/users'
    u = requests.post(user_endpoint, headers = headers, json = payload)
    id = json.loads(u.text)['id']

    payload2 = {
    "created_at": "2019-09-05T16:54:14Z",
    "duration": 60,
    #"host_id": str(id),
    "id": 1100000+index,
    "settings": {
        "alternative_hosts": "",
        "approval_type": 2,
        "audio": "both",
        "close_registration": False,
        "cn_meeting": False,
        "enforce_login": False,
        "enforce_login_domains": "",
        "global_dial_in_countries": [
        "US"
        ],
        "host_video": False,
        "in_meeting": False,
        #"join_before_host": True,
        "mute_upon_entry": False,
        "participant_video": False,
        "use_pmi": False,
        "waiting_room": False,
        "watermark": False,
    },
    "start_time": "2019-08-30T22:00:00Z",
    "status": "waiting",
    "timezone": "America/New_York",
    "topic": topic,
    "type": 2,
    }

    meeting_endpoint = 'https://api.zoom.us/v2/users/'+id+'/meetings'
    headers2 = {'Authorization': "Bearer " + access_token, 'host': 'zoom.us', "Content-Type": 'application/json'}
    x = requests.post(meeting_endpoint, headers = headers2, json = payload2)
    return (json.loads(x.text)['start_url'], json.loads(x.text)['join_url'],json.loads(x.text)['id'])

def get_participants(access_token, meeting_id):
    headers = {'Authorization': "Bearer " + access_token, 'host': 'zoom.us', "Content-Type": 'application/json'}
    endpoint = 'https://api.zoom.us/v2/metrics/meetings/' + str(meeting_id) + '/participants'
    x = requests.get(meeting_endpoint, headers = headers)
    return json.loads(x.text)['participants']

'''@background(schedule = 1)
def refresh_access_token():
    token = Token.objects.get(id = 1)
    refresh_token = token.refresh_token
    client_id = 'zJib8nQsTG0QA_JgEqj5Q'
    client_secret = 'V7GDiRa1c1d9gMRfW4GzZMvp3MJY7vkE'

    message = client_id + ':' + client_secret
    message_bytes = message.encode('ascii')
    base64_bytes = base64.b64encode(message_bytes)
    auth = 'Basic ' + base64_bytes.decode('ascii')

    endpoint = 'https://zoom.us/oauth/token?grant_type=refresh_token&refresh_token=' + refresh_token
    headers = {'Authorization': auth, 'host': 'zoom.us'}
    x = requests.post(endpoint, headers = headers)
    j = json.loads(x.text)
    token.refresh_token= j['refresh_token']
    token.access_token = j['access_token']
    token.save()
    print('\n')
    print('TOKEN HAS BEEN REFRESHED' + str(time.time()))
    print('\n')
    return'''
#schedule.every(5).seconds.do(refresh_access_token)

#while True:
#    schedule.run_pending()
#    time.sleep(1) 

def refresh_access_token():
    global start
    token = Token.objects.get(id = 1)
    refresh_token = token.refresh_token
    client_id = 'zJib8nQsTG0QA_JgEqj5Q'
    client_secret = 'V7GDiRa1c1d9gMRfW4GzZMvp3MJY7vkE'

    message = client_id + ':' + client_secret
    message_bytes = message.encode('ascii')
    base64_bytes = base64.b64encode(message_bytes)
    auth = 'Basic ' + base64_bytes.decode('ascii')

    endpoint = 'https://zoom.us/oauth/token?grant_type=refresh_token&refresh_token=' + refresh_token
    headers = {'Authorization': auth, 'host': 'zoom.us'}
    x = requests.post(endpoint, headers = headers)
    j = json.loads(x.text)
    token.refresh_token= j['refresh_token']
    token.access_token = j['access_token']
    token.count = start
    token.save()
    #print('\n')
    #print('TOKEN HAS BEEN REFRESHED' + str(time.time()))
    #print('\n')
    return


#class PostCreateView(CreateView):
#    model = Room
#   fields = ['notes']

#    def get_success_url(self):
#        return reverse('blog:detail', args=[self.object.pk])
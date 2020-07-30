from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Room
from .models import Profile, Token
from django.views.generic import CreateView
from .forms import NameForm
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
from background_task import background
import schedule
import time



#token = 'eyJhbGciOiJIUzUxMiIsInYiOiIyLjAiLCJraWQiOiIyNWYyMjA2YS1lODA3LTRlMjUtYjhjYi0wZGZjMjBhYjdiNWIifQ.eyJ2ZXIiOiI2IiwiY2xpZW50SWQiOiJ6SmliOG5Rc1RHMFFBX0pnRXFqNVEiLCJjb2RlIjoiZXVnNWlrSG9LZF95ZWlWdUlXc1FfNjNOOUtEY3F1aG9nIiwiaXNzIjoidXJuOnpvb206Y29ubmVjdDpjbGllbnRpZDp6SmliOG5Rc1RHMFFBX0pnRXFqNVEiLCJhdXRoZW50aWNhdGlvbklkIjoiMjM2NDJlMTFlYjBiZTFhZGNiMmFkYjZjNTFhOWJlNDkiLCJ1c2VySWQiOiJ5ZWlWdUlXc1FfNjNOOUtEY3F1aG9nIiwiZ3JvdXBOdW1iZXIiOjAsImF1ZCI6Imh0dHBzOi8vb2F1dGguem9vbS51cyIsImFjY291bnRJZCI6ImhORE8zbG1NU3RTNnhjcS1iMy1QMUEiLCJuYmYiOjE1OTQ0Mzc2NzQsImV4cCI6MTU5NDQ0MTI3NCwidG9rZW5UeXBlIjoiYWNjZXNzX3Rva2VuIiwiaWF0IjoxNTk0NDM3Njc0LCJqdGkiOiJiYWQxNjhjOS03YTc3LTRlYTMtOGI2OC1mZWUwMGIzNWE1ODkiLCJ0b2xlcmFuY2VJZCI6MjJ9.ztaR-aKWc0tiPkmbtwlYQUO92cwURNbXRQxNt_75uvex0rIlTVpQJajgj_TNx5uFheHLfcnCT0-0E13gRgXOHw'
start = 1300
def read_file(request):
    f = open('/Users/arulkapoor118/collab_website/collab/studyApp/loaderio-4049d7ee993d07bdda5b43856ece8ea9.txt', 'r')
    file_content = f.read()
    f.close()
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

        # course = ...
        Profile.objects.create(user=instance, room = Room.objects.get(title = "inactive"), zoom_id= "", section = "")

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
def createroom(request):
    if request.method == 'GET':
        title = request.GET['room_title']
        course = request.GET['course']
        print(course)
        form = NameForm()
        global start
        user = Profile.objects.get(user = request.user)
        #rooms = start_meeting(token, start, title, user.zoom_id)
        refresh_access_token()

        token = Token.objects.get(id = 1).access_token
        rooms = start_meeting(token, start, title, request.user.first_name, request.user.last_name)

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
    course = request.path[1:-1]
    user = request.user
    if course == "":
        course = 'LITHUM'
    elif course == 'section':
        #course = 'SECTION ABC'
        course = user.profile.section

    if user.username != user.get_full_name and user.username != 'arulkapoor118':
        user.username = str(user.get_full_name())
        user.save()
    c = Counter()

    form = NameForm()

    context = {
        #'rooms': Room.objects.all(),
        'rooms': Room.objects.filter(course = course),
        'users': Profile.objects.all(),
        'counter': c,
        'form': form,
    }
    return render(request, 'studyApp/index.html', context)

def login(request):
    return render(request, 'studyApp/login.html')

'''def logout(request):
    logout(request)
    return render('studyApp/index.html')'''

def joinroom(request):
    if request.method == 'GET':
        room = request.GET['room_id']
        user = Profile.objects.get(user = request.user)
        #user = Profile.objects.get(user__first_name = 'Lauren')
        user.room = Room.objects.get(meeting_id = room) 
        user.save()
        #zoom api call to get all meeting participants, and then loop over participant ids and check 
        return HttpResponse("success")
    else:
        return HttpResponse("Request method is not a GET")

def start_meeting(access_token, index, topic, firstname, lastname):
    global start
    start+=1
    #print(access_token)
    
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
    #print('\n')
    #print('TOKEN HAS BEEN REFRESHED' + str(time.time()))
    #print('\n')
    return
from django.urls import path, include
from . import views
from django.conf.urls import url
 




urlpatterns = [
    path('', views.home, name = "studyApp-home"),
    path('section/', views.home, name = "studyApp-home"),
    path('login/', views.login, name = "studyApp-login"),
    url(r'^joinroom/$', views.joinroom, name='joinroom'),
    url(r'^createroom/$', views.createroom, name='createroom'),
    url(r'^meetingend', views.meetingend, name='meetingend'),
    url(r'^participantleft', views.participantleft, name='participantleft'),
    #url(r'^participantjoin', views.participantjoin, name='participantjoin'),
    path('accounts/', include('allauth.urls')),
    url(r'^loaderio-4049d7ee993d07bdda5b43856ece8ea9/', views.read_file, name='loaderio-4049d7ee993d07bdda5b43856ece8ea9'),
    #url(r'^createMeeting', views.createMeeting, name = "createMeeting")
]

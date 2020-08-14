from django.urls import path, include
from . import views
from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', views.home, name = "studyApp-home"),
    path('section/', views.home, name = "studyApp-section"),
    path('login/', views.login, name = "studyApp-login"),
    path('classes/', views.classes, name = "studyApp-classes"),
    url(r'^joinroom/$', views.joinroom, name='joinroom'),
    url(r'^createroom/$', views.createroom, name='createroom'),
    url(r'^uploadImage/$', views.uploadImage, name='uploadImage'),
    url(r'^selectClass/$', views.selectClass, name='selectClass'),
    url(r'^meetingend', views.meetingend, name='meetingend'),
    url(r'^meetingstart', views.meetingstart, name='meetingstart'),
    url(r'^participantleft', views.participantleft, name='participantleft'),
    #url(r'^participantjoin', views.participantjoin, name='participantjoin'),
    path('accounts/', include('allauth.urls')),
    url(r'^loaderio-4049d7ee993d07bdda5b43856ece8ea9/', views.read_file, name='loaderio-4049d7ee993d07bdda5b43856ece8ea9'),
    #url(r'^createMeeting', views.createMeeting, name = "createMeeting")
]
handler404 = 'studyApp.views.my_custom_page_not_found_view'

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
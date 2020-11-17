from django.urls import path, include
from . import views
from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static




urlpatterns = [
    path('', views.home, name = "studyApp-home"),
    path('section/', views.home, name = "studyApp-section"),
    path('class1/', views.home, name = "studyApp-class1"),
    path('class2/', views.home, name = "studyApp-class2"),
    path('class3/', views.home, name = "studyApp-class3"),
    path('class4/', views.home, name = "studyApp-class4"),
    path('class5/', views.home, name = "studyApp-class5"),
    path('login/', views.login, name = "studyApp-login"),
    path('classes/', views.classes, name = "studyApp-classes"),
    #path('error/', views.error, name = "studyApp-error"),
    url(r'^joinroom/$', views.joinroom, name='joinroom'),
    url(r'^createroom/$', views.createroom, name='createroom'),
    url(r'^oauth/$', views.oauth, name='oauth'),
    url(r'^token/$', views.token, name='token'),
    url(r'^uploadImage/$', views.uploadImage, name='uploadImage'),
    url(r'^selectClass/$', views.selectClass, name='selectClass'),
    url(r'^meetingend', views.meetingend, name='meetingend'),
    url(r'^participantleft', views.participantleft, name='participantleft'),
    url(r'^authview/$', views.authview, name='authview'),
    #url(r'^participantjoin', views.participantjoin, name='participantjoin'),
    path('accounts/', include('allauth.urls')),
    url(r'^loaderio-4049d7ee993d07bdda5b43856ece8ea9/', views.read_file, name='loaderio-4049d7ee993d07bdda5b43856ece8ea9'),
    #url(r'^createMeeting', views.createMeeting, name = "createMeeting"),
    path('ckeditor/', include(
        'ckeditor_uploader.urls')),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
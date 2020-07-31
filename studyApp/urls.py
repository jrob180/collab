from django.urls import path, include
from . import views
from django.conf.urls import url




urlpatterns = [
    path('', views.home, name = "studyApp-home"),
    path('login/', views.login, name = "studyApp-login"),
    url(r'^joinroom/$', views.joinroom, name='joinroom'),
    path('accounts/', include('allauth.urls')),
    url(r'session_security/', include('session_security.urls')),
    #url(r'^createMeeting', views.createMeeting, name = "createMeeting")
]
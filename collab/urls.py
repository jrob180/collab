"""collab URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
<<<<<<< HEAD
from django.urls import path, include 
=======
from django.urls import path, include
#from studyApp.views import refresh_access_token

>>>>>>> 72e859f4aed96f3d3d32d870addda1ad98daf3c3

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('studyApp.urls')),
    path('accounts/', include('allauth.urls')),
    path(r'session_security/', include('session_security.urls')),
]

#refresh_access_token(repeat=2, repeat_until = None)


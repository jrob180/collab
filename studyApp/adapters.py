from allauth.socialaccount.adapter import DefaultSocialAccountAdapter
from allauth.exceptions import ImmediateHttpResponse
from django.shortcuts import render

class MySocialAccount(DefaultSocialAccountAdapter):
    def pre_social_login(self, request, sociallogin):
        u = sociallogin.user
        if not (u.email.split('@')[1] == "college.harvard.edu" or u.email.split('@')[1] == "gmail.com" or u.email.split('@')[1] == "columbia.edu"):
            raise ImmediateHttpResponse(render(request, 'studyApp/error.html'))

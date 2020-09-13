from allauth.socialaccount.adapter import DefaultSocialAccountAdapter
from django.shortcuts import render, redirect
from allauth.exceptions import ImmediateHttpResponse

import requests


class MySocialAccount(DefaultSocialAccountAdapter):
    def pre_social_login(self, request, sociallogin):
        u = sociallogin.user
        if not (u.email.split('@')[1] == "columbia.edu" or u.email.split('@')[1] == "college.harvard.edu"):
            raise ImmediateHttpResponse(render(request, 'studyApp/error.html'))

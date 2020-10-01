from allauth.socialaccount.adapter import DefaultSocialAccountAdapter
from django.shortcuts import render, redirect
from allauth.exceptions import ImmediateHttpResponse

import requests


class MySocialAccount(DefaultSocialAccountAdapter):
    def pre_social_login(self, request, sociallogin):
        u = sociallogin.user
        whitelist = ["columbia.edu", "barnard.edu", "tc.columbia.edu", "cumc.columbia.edu", "college.harvard.edu", "princeton.edu", "harvardconsulting.org"]
        email = u.email.split('@')[1]
        if not (email in whitelist):
            raise ImmediateHttpResponse(render(request, 'studyApp/error.html'))

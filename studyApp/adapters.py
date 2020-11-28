from allauth.socialaccount.adapter import DefaultSocialAccountAdapter
from django.shortcuts import render, redirect
from allauth.exceptions import ImmediateHttpResponse

import requests


class MySocialAccount(DefaultSocialAccountAdapter):
    def pre_social_login(self, request, sociallogin):
        u = sociallogin.user
        whitelist = ["columbia.edu", "barnard.edu", "tc.columbia.edu", "cumc.columbia.edu", "college.harvard.edu", "fas.harvard.edu", "cornell.edu",
         "princeton.edu", "alumni.princeton.edu", "harvardconsulting.org", "yale.edu", "brown.edu", "alumni.brown.edu", "mit.edu", "sas.upenn.edu", "seas.upenn.edu", "wharton.upenn.edu", "dartmouth.edu"]
        email = u.email.split('@')[1]
        if not (email in whitelist):
            raise ImmediateHttpResponse(render(request, 'studyApp/error.html'))

from allauth.socialaccount.adapter import DefaultSocialAccountAdapter

class MySocialAccount(DefaultSocialAccountAdapter):
    def pre_social_login(self, request, sociallogin):
        u = sociallogin.user
        if not u.email.split('@')[1] == "columbia.edu":
            raise ImmediateHttpResponse(render_to_response('error.html'))

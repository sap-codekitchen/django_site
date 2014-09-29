from django import forms
from django.contrib.auth import authenticate
from django.contrib.auth.models import User

from django.core.exceptions import ObjectDoesNotExist

class AuthForm(forms.Form):
    email = forms.EmailField()
    password = forms.CharField()

    error_messages = {
        'invalid_user': "There is no user account with that email.",
        'invalid_login': "That is not the correct password for this account"
            }

    def __init__(self, request=None, *args, **kwargs):
        self.request = request
        self.user_cache = None
        super(AuthForm, self).__init__(*args, **kwargs)

    def clean(self):
        # we treat the email as the username
        email = self.cleaned_data.get('email')
        password = self.cleaned_data.get('password')

        if email and password:
            # first check if the user exists
            try:
                User.objects.get(username=email)
            except ObjectDoesNotExist:
                raise forms.ValidationError(
                        self.error_messages['invalid_user'],
                        code='invalid_user'
                        )

            # if the user exists, try authenticating
            self.user_cache = authenticate(username=email,
                                           password=password)
            if self.user_cache is None:
                raise forms.ValidationError(
                        self.error_messages['invalid_login'],
                        code='invalid_login',
                        )
        return self.cleaned_data

    def get_user(self):
        return self.user_cache



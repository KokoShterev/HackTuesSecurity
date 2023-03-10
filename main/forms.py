from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class CreateNewPassword(forms.Form):
    website = forms.CharField(label="Website", max_length=200)
    website_password = forms.CharField(label="Password", max_length=200)


class Register(UserCreationForm):
    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]

from django import forms
from authentication_src.models import SchoolManagerModel
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import AuthenticationForm



class Signup_form(UserCreationForm):
    class Meta:
        model = get_user_model()
        fields = ['username', 'role', 'tel']

class Login_form(forms.Form):
    username = forms.CharField(max_length=255)
    password = forms.CharField(max_length=255, widget=forms.PasswordInput)

class Updater_form(forms.ModelForm):
    class Meta:
        model = get_user_model()
        fields = ['username', 'role', 'tel', 'password']

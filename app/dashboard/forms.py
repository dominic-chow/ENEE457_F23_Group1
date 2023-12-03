from django import forms
from .models import DoctorGroup
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class DoctorGroupForm(forms.ModelForm):
    class Meta:
        model = DoctorGroup
        fields = ['name', 'members']


class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')


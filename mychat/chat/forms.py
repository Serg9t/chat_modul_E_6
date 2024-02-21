from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

from chat.models import User, Room


class SingUpForm(UserCreationForm):

    class Meta:
        model = get_user_model()
        fields = ['username', 'password1', 'password2']


class UserLoginFrom(AuthenticationForm):

    class Meta:
        model = get_user_model()
        fields = ['username', 'password']


class ProfileUserForm(forms.ModelForm):

    class Meta:
        model = get_user_model()
        fields = ['photo', 'username']
        labels = {
            'username': 'Name',
            'photo': 'Avatar',
        }


class RoomForm(forms.ModelForm):
    class Meta:
        model = Room
        fields = ['name', 'slug']

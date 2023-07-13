# from django import forms
from django.contrib.auth.forms import PasswordChangeForm, UserCreationForm
# from django.forms import ModelForm

from .models import User


class RegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'email', 'password1', 'password2']


class PasswordForm(PasswordChangeForm):

    def save(self, commit=True):
        password = self.cleaned_data['new_password1']
        self.user.set_password(password)
        self.user.save()
        return self.user


# class UserForm(ModelForm):
#     class Meta:
#         model = User
#         fields = ['first_name', 'last_name', 'username', 'email', 'password']
#

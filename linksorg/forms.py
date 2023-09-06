from django import forms
from django.contrib.auth.forms import PasswordChangeForm, UserCreationForm
from django.forms import ModelForm

from .models import User, Link


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


class AddLinkForm(forms.Form):
    BOOL = (
        (True, 'Important'),
        (False, 'Average')
    )
    url_link = forms.CharField(max_length=250)
    category = forms.CharField(max_length=100)
    short_definition = forms.CharField(max_length=200)
    important = forms.ChoiceField(choices=BOOL)


# class UserForm(ModelForm):
#     class Meta:
#         model = User
#         fields = ['first_name', 'last_name', 'username', 'email', 'password']
#

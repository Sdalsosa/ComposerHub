from django.forms import ModelForm, widgets
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Profile

class NewUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'username', 'password1', 'password2']


    def __init__(self, *args, **kwargs):
        super(NewUserForm, self).__init__(*args,**kwargs)

        self.fields['username'].widget.attrs.update({'class': 'input', 'placeholder': 'Enter Username'})
        self.fields['first_name'].widget.attrs.update({'class': 'input', 'placeholder': 'Enter First Name'})
        self.fields['last_name'].widget.attrs.update({'class': 'input', 'placeholder': 'Enter Last Name'})
        self.fields['email'].widget.attrs.update({'class': 'input', 'placeholder': 'Enter your email'})
        self.fields['password1'].widget.attrs.update({'class': 'input', 'placeholder': 'Enter Password'})
        self.fields['password2'].widget.attrs.update({'class': 'input', 'placeholder': 'Re-enter Password'})


class AccountForm(ModelForm):
    class Meta:
        model = Profile
        fields = ['first_name', 'last_name', 'email', 'username', 'about', 'profile_image', 'website']
    
    def __init__(self, *args, **kwargs):
        super(AccountForm, self).__init__(*args,**kwargs)

        self.fields['username'].widget.attrs.update({'class': 'input', 'placeholder': 'Enter Username'})
        self.fields['first_name'].widget.attrs.update({'class': 'input', 'placeholder': 'Enter First Name'})
        self.fields['last_name'].widget.attrs.update({'class': 'input', 'placeholder': 'Enter Last Name'})
        self.fields['email'].widget.attrs.update({'class': 'input', 'placeholder': 'Enter your email'})
        self.fields['about'].widget.attrs.update({'class': 'input', 'placeholder': 'Enter Biography'})
        self.fields['website'].widget.attrs.update({'class': 'input', 'placeholder': 'Enter website'})
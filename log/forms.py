from django import forms
from log import models 
from django.contrib.auth.models import User
import datetime


class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    class Meta():
        model = User
        fields = ('username', 'password','email')

#class UserProfileInfoForm(forms.ModelForm):
 #   class Meta():
  #      model = UserProfileInfo
   #     fields = ('portfoliosite','profile_pic')
        

class ticketform(forms.Form):
    date = forms.DateField(initial=datetime.date.today)
    Subject = forms.CharField( label='Subject' max_length=100 )
    Message = forms.CharField(widget=forms.Textarea)
    
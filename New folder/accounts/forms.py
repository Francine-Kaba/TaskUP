from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User

class SignUpForm(UserCreationForm):
    first_name = forms.CharField(
        widget=forms.TextInput(
            attrs={'class': 'form-control'
                   }))
    
    last_name = forms.CharField(
        widget=forms.TextInput(
            attrs={'class': 'form-control'
                   }))
    
    username = forms.CharField(
        widget=forms.TextInput(
            attrs={'class': 'form-control'
                   }))
    
    email = forms.CharField(
        widget=forms.TextInput(
            attrs={'class': 'form-control'
                   }))
    
    password1: forms.CharField(
        widget=forms.PasswordInput(
            attrs={'class': 'form-control'
            }))
    
    password2: forms.CharField(
        widget=forms.PasswordInput(
            attrs={'class': 'form-control'
            }))
    
    class Meta:
        model = User
        fields = ('first_name','last_name','username','phone_number','email','password1','password2')
        
    
from dataclasses import field
from django import forms
from . import models

class PatientAct(forms.ModelForm):
    class Meta:
        model = models.PatientActivities
        fields=['appointment_type', 'appointment_date', 'doctor']
        
        
# class DoctorSign(UserCreationForm):
#     class Meta:
#         model = models.DoctorSign
#         fields = ('full_name','username','phone_number','password')
        



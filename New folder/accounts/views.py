from django.shortcuts import render, redirect
from .forms import SignUpForm
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from .models import User, Doctor, PatientActivities
import string
from django.db import connection
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from . import forms
from django.contrib.auth import views as auth_views

letters = string.ascii_letters + string.punctuation

# Create your views here.
def homepage(request):
    return render(request, 'embeddedapp/homepage.html')
def signup_view(request):
    if request.method == 'POST':
        phone = str(request.POST['phone_number'])
        form = SignUpForm(request.POST)
        if form.is_valid():
            if User.objects.filter(phone_number=phone).exists():
                messages.info(request, 'Phone number exists.')
                return redirect('embedded_app:signup')
            else:
                for item in phone:    
                    if item in letters:
                        messages.info(request, 'Please enter a valid phone number.')
                        return redirect('embedded_app:signup')
            form.save()
            return redirect('embedded_app:signin')
    else:
        form = SignUpForm()
    return render(request, 'embeddedapp/register.html', {'form': form})

@csrf_exempt
def signin_view(request):
    if request.method == 'POST':
        identity_type = request.POST['identity']
        username = request.POST['username']
        password = request.POST['password']
        form = AuthenticationForm(data = request.POST)
        if form.is_valid():
            user = form.get_user()
            if 'next' in request.POST:
                return redirect(request.POST.get('next'))
            else:
                if identity_type == "":
                    messages.info(request, "Select an identity")
                    return redirect('embedded_app:signin')
                elif identity_type == 'patient':
                    login(request, user)
                    return redirect('embedded_app:patient')
                elif identity_type == 'doctor':
                    login(request, user)
                    return redirect('embedded_app:docs')
                elif identity_type == 'admin':
                    if username == 'ad_min' and password == 'pass_word':
                        login(request, user)
                        return redirect('embedded_app:admin')
                    else:
                        messages.info(request,'You are not an admin')
                        return redirect('embedded_app:signin')
    else:
        form = AuthenticationForm() 
    return render(request, 'embeddedapp/login.html', {'form':form})

@login_required(login_url='embedded_app:signin')
def patient_view(request):
    doctors = Doctor.objects.all()
    if request.method == 'POST':
        form = forms.PatientAct(request.POST)
        if request.POST.get('doctor'):
            doctor_value = Doctor()
            doctor_value.doctor  = request.POST.get('doctor')
            doctor_value.save()
        if form.is_valid():
            instance = form.save(commit=False)
            instance.user = request.user
            instance.save()
            return redirect('embedded_app:patient')
    else:
        form = forms.PatientAct(request.POST)   
    return render(request, 'embeddedapp/patient.html', {'form':form, 'doctors':doctors})



def doctor_appointment_view(request):
    appointments = PatientActivities.objects.all()
    return render(request, 'embeddedapp/doctor_appointments.html', {'appointments':appointments})

    

# Doctor views 
def doctor_view(request):

    return render(request, 'embeddedapp/doctor.html', {})

def emergency_view(request):
    return render(request, 'embeddedapp/doc_emergency.html', {})

def message_view(request):
    return render(request, 'embeddedapp/doc_message.html', {})

def admin_view(request):
    doctors = Doctor.objects.all()
    return render(request, 'embeddedapp/admin.html', {'doctors':doctors})

def admin_message_view(request):
    return render(request, 'embeddedapp/admin_message.html',{})

def admin_doc_view(request):
    doctors = Doctor.objects.all()
    return render(request, 'embeddedapp/admin_doc.html', {'doctors':doctors})

def admin_analytics_view(request):
    return render(request, 'embeddedapp/admin_analytics.html')

def logout_view(request):
    logout(request)
    return redirect('embedded_app:signin')


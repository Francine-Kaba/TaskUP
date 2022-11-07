from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    phone_number = models.CharField(max_length=10, blank=False)
    date_created = models.DateField(auto_now_add=True)
    


class PatientActivities(models.Model):
    appointment_type = models.CharField(max_length=20, blank=False)
    appointment_date = models.DateTimeField(auto_now_add=False, null=False, blank=False)
    doctor = models.CharField(max_length=20, blank=False)
    user = models.ForeignKey(User, default=None, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.appointment_type
    

class Doctor(models.Model): 
    full_name = models.CharField(max_length=255, blank= False, null=False)
    username = models.CharField(max_length=15, blank=False, null=False)
    phone_number = models.CharField(max_length=10, blank=False, null=False)
    password = models.CharField(max_length=50, blank=False, null=False)
    
    def __str__(self):
        return self.full_name
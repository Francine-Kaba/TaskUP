from django.contrib import admin
from .models import User, PatientActivities, Doctor

# Register your models here.
admin.site.register(User)
admin.site.register(PatientActivities)
admin.site.register(Doctor)
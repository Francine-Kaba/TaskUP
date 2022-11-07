from django.shortcuts import render

# Create your views here.
def patient_news_view(request):
    return render(request, 'embeddedapp/newsfeed.html', {})


def doctor_view(request):
    return render(request, 'embeddedapp/doctor.html', {})

def admin_view(request):
    return render(request, 'embeddedapp/admin.html', {})

from django.urls import path
from accounts import views

app_name = 'embedded_app'

urlpatterns = [
    path('register/',views.signup_view,name='signup'),
    path('login/',views.signin_view, name = 'signin'),
    path('patient/',views.patient_view, name='patient'),
    path('appointments/',views.doctor_appointment_view, name='appointments'),
    path('doc/',views.doctor_view, name='docs'),
    path('emergency/', views.emergency_view, name='emergency'),
    path('message/',views.message_view, name='message'),
    path('admin/', views.admin_view, name='admin'),
    path('admin_messages/',views.admin_message_view, name='admin_messages'),
    path('admin_doc/',views.admin_doc_view, name='admin_doc'),
    path('admin_analytics/',views.admin_analytics_view, name='admin_analytics'),
    path('logout/', views.logout_view, name='logout'),
]
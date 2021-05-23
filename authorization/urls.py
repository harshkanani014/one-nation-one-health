from django.contrib.auth import login
from django.urls import path
from . import views

urlpatterns = [
    path("", views.home_page, name="home_page"),
    path("register", views.register, name="register"),
    path("verify_otp", views.verify_otp, name="otp_verify"),
    path('logout', views.logout_view, name="logout"),
    path('login', views.signin, name="signin"),
    path('patient_index', views.patient_index, name="patient"),
    path('doctor_index', views.doctor_index, name="doctor"),
    path('pharmacist_index', views.pharmacist_index, name="pharmacist")
]
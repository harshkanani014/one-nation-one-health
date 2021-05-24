from django.contrib.auth import login
from django.urls import path
from . import views

urlpatterns = [
      path('/enter_patient_record', views.add_record, name="patientRecord")
]
from django.db import models
from django.db.models.expressions import F
from jsonfield import JSONField
from django.conf import settings

#from one_health.authorization.models import CustomUser

# from django.apps import apps
# CustomUser = apps.get_model("authorization", "CustomUser")


# Create your models here.
class Medicine(models.Model):
    medicine_brand = models.TextField(max_length=500)
    medicine_name = models.TextField(max_length=500)
    medicine_price = models.IntegerField()
    medicine_category = models.TextField(max_length=500)
    medicine_usage = models.TextField(max_length=100)
    medicine_side_effect = models.TextField(max_length=100)


class HealthRecord(models.Model):
    user_details = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, default=0)
    patient_name = models.TextField(max_length=500)
    patient_age = models.IntegerField()
    patient_gender = models.TextField(max_length=100, default="None")
    doctor_fees = models.IntegerField()
    payment_method = models.TextField(max_length=100, default="None")
    prescription = models.TextField(max_length=1000)
    medicine = models.TextField(max_length=1000, default="None")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

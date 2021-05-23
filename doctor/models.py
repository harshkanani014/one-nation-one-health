from django.db import models
from jsonfield import JSONField
import jsonfield
# Create your models here.
class Medicine(models.Model):
    medicine_brand = models.TextField(max_length=500)
    medicine_name = models.TextField(max_length=500)
    medicine_price = models.IntegerField()
    medicine_category = models.TextField(max_length=500)
    medicine_usage = models.TextField(max_length=100)
    medicine_side_effect = models.TextField(max_length=100)

class paymentMethod(models.Model):
    payment_method = models.TextField()

class gender(models.Model):
    patient_gender = models.TextField(max_length=50, null=True)

class HealthRecord(models.Model):
    patient_name = models.TextField(max_length=500)
    patient_age = models.IntegerField()
    patient_genderr = models.ForeignKey(gender, on_delete=models.CASCADE, null=True)
    doctor_fees = models.IntegerField()
    payment_method = models.ForeignKey(to=paymentMethod, on_delete=models.CASCADE, related_name="payment")
    prescription = models.TextField(max_length=1000)
    medicine = JSONField(default=dict())
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

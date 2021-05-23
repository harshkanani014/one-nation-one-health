from django.contrib import admin
from .models import gender, HealthRecord, Medicine, paymentMethod

admin.site.register(gender)
admin.site.register(HealthRecord)
admin.site.register(Medicine)
admin.site.register(paymentMethod)
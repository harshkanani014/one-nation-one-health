from django.contrib import admin
from .models import HealthRecord, Medicine

admin.site.register(HealthRecord)
admin.site.register(Medicine)

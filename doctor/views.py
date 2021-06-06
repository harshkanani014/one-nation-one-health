from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from authorization.models import CustomUser
from .models import HealthRecord, Medicine

@login_required(login_url="/")
def add_record(request):
    print(request.session['mob'])
    if request.method=="POST":
        phone = request.session['mob']
        user_num = phone['mob']
        patient_name = request.POST.get('patient_name')
        patient_gender = request.POST.get('patient_gender')
        patient_age = request.POST.get('patient_age') 
        doctor_fees = request.POST.get('doctor_fees')
        payment_method =  request.POST.get('payment_method')
        prescription = request.POST.get('prescription')
        medicine = request.POST.get('medicine')
        user_data = CustomUser.objects.get(mobile=user_num)
        new_health_record = HealthRecord()
        new_health_record.user_details = user_data
        new_health_record.patient_name = patient_name
        new_health_record.patient_gender = patient_gender
        new_health_record.patient_age = patient_age
        new_health_record.doctor_fees = doctor_fees
        new_health_record.payment_method = payment_method
        new_health_record.prescription = prescription
        #new_health_record.medicine = medicine
        new_health_record.save()
        #request.session.flush()
        return redirect("/doctor_index")
    else:
        # user_num = request.session['mob']
        # print(user_num) 
        # all_med = Medicine.objects.all()
        # med = []
        # for i in all_med:
        #     med.append(i.medicine_name)
        # print(med)
        # context = {
        #     'med':med
        # }
        return render(request, "doctor/record_entry.html")
        
        


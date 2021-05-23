from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout, get_user
from django.contrib.auth.models import User, auth
from .models import CustomUser
from django.contrib import messages
import time
import pyotp
import base64
import random
from django.contrib.auth.decorators import login_required
from twilio.rest import Client
# Create your views here.

def send_sms(otp, to_):

    # Your Account SID from twilio.com/console
    account_sid = "AC3c6ea125b0591da78e21e3ae78ac184c"
    # Your Auth Token from twilio.com/console
    auth_token  = "ae6a5ac6219966cc2fa89f476d522ce2"

    client = Client(account_sid, auth_token)
    #print(to_)
    message = client.messages.create(
        to="+91" + str(to_), 
        from_="+12105298397",
        body="Your otp is " + str(otp)  + " only valid for 1 mins ")

    #print(message.sid)


def home_page(request):
    return render(request, "accounts/index.html")

def register(request):
    if request.method=="POST":
        name = request.POST.get('name')
        phone = request.POST.get('phoneNumber')
        patient = request.POST.get('patient')
        doctor = request.POST.get('doctor')
        pharmacist = request.POST.get('pharmacist')
        is_patient = False
        is_doctor = False
        is_pharmacist = False
        if doctor==None and pharmacist==None:
            is_patient = True
        elif patient==None and pharmacist==None:
            is_doctor = True
        else:
            is_pharmacist = True

        try:
            find_phone = CustomUser.objects.get(mobile=phone)
            messages.warning(request, "Phone number already exist")
            return redirect("/register")
        except:
                print(name, phone)
                otp = random.randint(1000, 9999)
                #send_sms(otp, phone)
                print("OTP :", otp)
                if is_patient:
                    request.session['mob'] = {'name': name, 'mob':phone, 'is_patient': is_patient}
                if is_doctor:
                    request.session['mob'] = {'name': name, 'mob':phone, 'is_doctor': is_doctor}
                if is_pharmacist:
                    request.session['mob'] = {'name': name, 'mob':phone, 'is_pharmacist': is_pharmacist}
                request.session['otp'] = otp
                expire_at = time.time() + 50
                request.session['exp'] = expire_at
                context = {
                            'var_phone': phone
                        }
                return render(request, "accounts/verification.html", context)
    else:
        return render(request, "accounts/register.html")

def signin(request):
    if request.method=="POST":
        phone = request.POST.get('phoneNumber')
        try:
            find_phone = CustomUser.objects.get(mobile=phone)
            otp = random.randint(1000, 9999)
            #send_sms(otp, phone)
            print("OTP :", otp)
            request.session['mob'] = {'mob':phone}
            request.session['otp'] = otp
            expire_at = time.time() + 50
            request.session['exp'] = expire_at
            context = {
                        'var_phone': phone
                    }
            return render(request, "accounts/verification.html", context)
        except:
            return redirect("/register")

    else:
        return render(request, "accounts/login.html")

    
def verify_otp(request):
    if request.method=="POST":
        if request.session.get('mob', None):
            if time.time()>request.session['exp']:
                context = {
                    'var_phone': request.session['mob']['mob']
                }
                messages.warning(request, 'OTP was expired!')
                return render(request,"accounts/verification.html",context)
            elif(request.session['otp'] == int(request.POST.get('otp'))):
                try:
                    user_data = request.session['mob']
                    new_user = CustomUser()
                    new_user.name = user_data['name']
                    new_user.mobile = user_data['mob']
                    if 'is_patient' in user_data:
                        new_user.is_patient = user_data['is_patient']
                    elif 'is_doctor' in user_data:
                        new_user.is_doctor = user_data['is_doctor']
                    elif 'is_pharmacist' in user_data:
                        new_user.is_pharmacist = user_data['is_pharmacist']
                    new_user.save()
                    request.session.flush()
                    login(request, new_user)
                    if new_user.is_patient:
                        return redirect("/patient_index")
                    if new_user.is_doctor:
                        return redirect("/doctor_index")
                    if new_user.is_pharmacist:
                        return redirect("/pharmacist_index")
                except:
                    user_data = request.session['mob']
                    user = CustomUser.objects.get(mobile=user_data['mob'])
                    request.session.flush()
                    login(request, user)
                    if user.is_patient:
                        return redirect("/patient_index")
                    if user.is_doctor:
                        return redirect("/doctor_index")
                    if user.is_pharmacist:
                        return redirect("/pharmacist_index")
            else:
                messages.warning(request, 'OTP was wrong!')
                return redirect("/otp_verify")
        else:
            response = redirect('/')
            return response
    else:
        response = redirect('/')
        return response

@login_required(login_url="/")
def patient_index(request):
    return render(request, "patient/patient_index.html")

@login_required(login_url="/")
def doctor_index(request):
    return render(request, "doctor/doctor_index.html")

@login_required(login_url="/")
def pharmacist_index(request):
    return render(request, "pharmacist/pharmacist_index.html")

def logout_view(request):
    logout(request)
    return redirect("/")


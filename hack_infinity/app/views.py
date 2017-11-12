from random import randint
from django.contrib.auth import login, logout
from django.shortcuts import render, get_object_or_404, redirect, render_to_response
from django.contrib.auth.models import User
from django.utils import timezone
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import update_last_login
from django.core.exceptions import ObjectDoesNotExist
from .models import *
import requests
from django.contrib import auth

# Create your views here.


def register(request):
    if request.method == 'POST':
        first_name = request.POST.get('fname')
        last_name = request.POST.get('lname')
        email = request.POST.get('email')
        user_type = request.POST.get('user_type')
        mobile = request.POST.get('mobile')
        aadhar = request.POST.get('aadhar')
        password = randint(1000, 9999)
        #message = "Your OTP for login is: "
        #requests.get('https://control.msg91.com/api/sendhttp.php?authkey=132727AshR9z6QU9Dg58416307&mobiles='+mob+'&message='+a+'&sender=DLFIND&route=4', None)
        if MyUser.objects.filter(email=email).exists():
            return render(request, 'register.html', {'error1': 'Email already taken by another user', 'first_name': first_name, 'last_name': last_name, 'username': username, 'email': email})
        elif MyUser.objects.filter(mobile_no=mobile).exists():
            return render(
                request,
                'register.html',
                {
                    'error': 'Mobile already registered by another user',
                    'first_name': first_name,
                    'last_name': last_name,
                    'username': username,
                    'email': email
                }
            )
        else:
            user = MyUser.objects.create(
                first_name=first_name, last_name=last_name, email=email, username=email, mobile_no=mobile, user_type=user_type)
            user.set_password(password)
            user.save()
            return redirect('/login/')
    else:
            return render(request, 'register.html')


@login_required
def query_produce(request):
    produce = Produce.objects.all()
    return render(request, "market.html", {"produce": produce})


@login_required
def add_support(request):
    if request.method == "POST":
        Support.objects.create(
            request.user,
            request.POST["support_text"]
        )
        return redirect("/index/")  # return the actual page, later
    else:
        return HttpResponse(status_code=400)

@login_required
def view_support(request):
    if request.method == "GET":
        support = Support.objects.filter(user_id=request.user.id)
        return render(request, "support.html", {"support": support})
    else:
        return HttpResponse(status_code=400)


@login_required
def remove_produce(request):
    if request.method == "POST":
        if (request.post.get("delete", None)):
            produce_id = request.POST["produce_id"]
            produce = Produce.objects.get(id=produce_id)
            produce.delete()
            return HttpResponse()
    return HttpResponse(status_code=400)


@login_required
def add_produce(request):
    if request.method == 'POST':
        crop = request.POST['crop']
        quantity = request.POST['quantity']
        produce = Produce(user=request.user, crop=crop, quantity=quantity)
        produce.save()
        return render(request, "market.html")
    else:
        return HttpResponse(status_code=400)


def login_app(request):
    if request.method == 'POST':
        mobile = request.POST.get('mobile')
        otp = request.POST.get('otp',None)
        #print(mobile + ' ' + otp)
        if 'mobile' in request.POST and otp is not None:
            try:
                user = MyUser.objects.get(mobile_no=mobile)
            except MyUser.DoesNotExist:
                return redirect('../register')
            email = user.email
            user = None
            user = auth.authenticate(
                username=email, password=str(otp))
            #print(user)
            if user:
                login(request, user)
                return redirect('../')
            else:
                return render(request, 'login.html', {'mobile': mobile, 'error': 'Incorrect OTP'})
        elif 'mobile' in request.POST and otp is None:
            mobile = request.POST.get('mobile')
            otp = str(randint(1000, 9999))
            try:
                user = MyUser.objects.get(mobile_no=mobile)
            except MyUser.DoesNotExist:
                print(mobile)
                return redirect('../register')
            user.set_password(otp)
            user.save()
            message = "Your OTP for login is: " + otp
            requests.get('https://control.msg91.com/api/sendhttp.php?authkey=132727AshR9z6QU9Dg58416307&mobiles=' +
                         mobile + '&message=' + message + '&sender=CROPPY&route=4', None)
            return HttpResponse()
    else:            
        return render(request, 'login.html')


def index(request):
    if request.user.is_authenticated():
        return render(request,'index.html')
    else:
        return redirect('../login')


def logout_app(request):
    if request.user.is_authenticated():
        logout(request)
        return redirect('../login/')
    else:
        return HttpResponseRedirect('../login/')

def feedback(request):
    if request.user.is_authenticated():
        if request.method == 'POST':
            aadhar = request.POST.get('aadharNumber')
            phoneNo = request.POST.get('phoneNo')
            text_feedback = request.POST.get('text_feedback')
            feedback = Support()
            feedback.user = request.user
            #feedback.aadhar = aadhar
            feedback.support_text = text_feedback
            feedback.is_read = False
            feedback.save()
    return render(request,'feedback.html')


def predictions(request):
    return render(request,'predictions.html')

def market(request):
    return render(request,'market.html')
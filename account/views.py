from django.shortcuts import render
from django.core.mail import send_mail
from django.http import HttpResponseRedirect,HttpResponse
from django.conf import settings
from django.contrib import auth
from django.contrib.auth.models import User
from .forms import login_form,name_form,password_form,user_change_form,account_creation_form
# Create your views here.
def signup(request):
    if request.method=="POST":
        fm=account_creation_form(request.POST)
        if fm.is_valid():
            email=fm.cleaned_data['email']
            fm.save()
            return render(request,'account.html')
        else:
            fm=account_creation_form()
            return render(request,'ok.html',{'fm':fm})
    else:
        fm=account_creation_form()
        return render(request,'signup.html',{'fm':fm})

def login(request):
    if request.method=='POST':
        user_fm=login_form(data=request.POST)
        if user_fm.is_valid():
            uname=user_fm.cleaned_data['username']
            upass=user_fm.cleaned_data['password']
            user=auth.forms.authenticate(username=uname,password=upass)
            if user is not None:
                auth.login(request,user)
                return HttpResponseRedirect('account')
            else:
                user_fm=login_form()
                return render(request,'ok.html',{'fm':user_fm})
        else:
                user_fm=login_form()
                return render(request,'ok.html',{'fm':user_fm})
    else:
        user_fm=login_form()
        return render(request,'login.html',{'fm':user_fm})

def account(request):
    if request.user.is_authenticated:
        user_acc=user_change_form(instance=request.user)
        return render(request,'account_detail.html',{'data':user_acc})
    else:
        return HttpResponseRedirect('login')

def password(request):
    if request.method=="POST":
        fm=password_form(user=request.user,data=request.POST)
        if fm.is_valid():
            fm.save()
            return HttpResponseRedirect('login')
        else:
            fm=password_form(request.user)
            return render(request,'password.html',{'fm':fm})
    else:
        fm=password_form(request.user)
        return render(request,'password.html',{'fm':fm})

def editaccount(request):
    if request.user.is_authenticated:
        if request.method=="POST":
            user=user_change_form(request.POST,instance=request.user)
            if user.is_valid():
                user.save()
                return HttpResponseRedirect('login')
            else:
                user_acc=user_change_form(instance=request.user)
                return render(request,'editprofile.html',{'data':user_acc})
        else:
            user_acc=user_change_form(instance=request.user)
            return render(request,'editprofile.html',{'data':user_acc})
    else:
        return HttpResponseRedirect('login')

def logout(request):
    auth.logout(request)
    return HttpResponseRedirect('login')

def passwordchange(request):
    if request.method=="POST":
        fm=name_form(data=request.POST)
        if fm.is_valid():
            upass=fm.cleaned_data['name']
            v=User.objects.get(username=upass)
            if v:
                return HttpResponseRedirect('password')
            else:
                return render(request,'ok.html')
        else:
            return render(request,'ok.html')
    else:
        fm=name_form()
        return render(request,'resetpassword.html',{'fm':fm})
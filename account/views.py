from django.shortcuts import render,redirect
from django.http import HttpResponseRedirect,HttpResponse
from django.contrib import auth
from django.contrib.auth.models import User
from .forms import login_form,name_form,password_form,user_change_form,account_creation_form
from django.contrib import messages
from django.contrib.auth.forms import PasswordResetForm
from django.db.models.query_utils import Q
from django.utils.http import urlsafe_base64_encode
from django.contrib.auth.tokens import default_token_generator
from django.utils.encoding import force_bytes
from django.conf import settings
from django.template.loader import render_to_string
from django.core.mail import send_mail, BadHeaderError

def signup(request):
    if request.method=="POST":
        fm=account_creation_form(request.POST)
        if fm.is_valid():
            fm.save()
            return render(request,'master/account.html')
        else:
            fm=account_creation_form()
            messages.success(request,'username is already exists')
            return render(request, "master/signup.html", {'fm':fm})
    else:
        fm=account_creation_form()
        return render(request,'master/signup.html',{'fm':fm})

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
                messages.success(request,'username or password is invalid')
                return render(request, "master/login.html", {'fm':user_fm})
        else:
            user_fm=login_form()
            messages.success(request,'username and password does not match')
            return render(request, "master/login.html", {'fm':user_fm})
    else:
        user_fm=login_form()
        return render(request,'master/login.html',{'fm':user_fm})

def account(request):
    if request.user.is_authenticated:
        user_acc=user_change_form(instance=request.user)
        return render(request,'master/account_detail.html',{'data':user_acc})
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
            return render(request,'master/password.html',{'fm':fm})
    else:
        fm=password_form(request.user)
        return render(request,'master/password.html',{'fm':fm})

def editaccount(request):
    if request.user.is_authenticated:
        if request.method=="POST":
            user=user_change_form(request.POST,instance=request.user)
            if user.is_valid():
                user.save()
                return HttpResponseRedirect('login')
            else:
                user_acc=user_change_form(instance=request.user)
                return render(request,'master/editprofile.html',{'data':user_acc})
        else:
            user_acc=user_change_form(instance=request.user)
            return render(request,'master/editprofile.html',{'data':user_acc})
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
                return render(request,'master/ok.html')
        else:
            return render(request,'master/ok.html')
    else:
        fm=name_form()
        return render(request,'master/resetpassword.html',{'fm':fm})

def password_reset_request(request):
    if request.method == "POST":
        password_reset_form = PasswordResetForm(request.POST)
        if password_reset_form.is_valid():
            data = password_reset_form.cleaned_data['email']
            associated_users = User.objects.filter(Q(email=data))
            if associated_users.exists():
                for user in associated_users:
                    subject = "Password Reset Requested"
                    email_template_name = "master/password_reset_email.txt"
                    c = {
					"email":user.email,
					'domain':'groupchat.ind.in',
					'site_name': 'Website',
					"uid": urlsafe_base64_encode(force_bytes(user.pk)),
					"user": user,
					'token': default_token_generator.make_token(user),
					'protocol': 'http',
					}
                    email = render_to_string(email_template_name, c)
                    vemail="www.consultandcounsel.com/reset/"+c['uid']+"/"+c['token']
                    print(vemail)
                    try:
                        send_mail(subject, email, 'admin@example.com' , [user.email], fail_silently=False)
                    except BadHeaderError:
                        return HttpResponse('Invalid header found.')
                    return redirect ("/password_reset/done/")
    password_reset_form = PasswordResetForm()
    return render(request=request, template_name="master/password_reset.html", context={"password_reset_form":password_reset_form})
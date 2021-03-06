from django.shortcuts import render
from django.conf import settings
from .form import feedbackform,digitalform,internform
from .models import Donation
from services.models import Transaction
from .models import Freesession,Internship
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect,HttpResponse,FileResponse
from django.contrib import auth
from django.views.decorators.csrf import csrf_exempt
from django.core.mail import send_mail
import razorpay
from django.views import View

def home(request):
    return render(request,'master/home.html')

def donation(request):
    return render(request,'master/donation.html')

def razorpaygateway(request):
    if request.method == "GET":
        return render(request,'master/razorpaygateway.html')
    else:
        username = request.POST['username']
        email = request.POST['email']
        amount = int(request.POST['amount'])
        donation = Donation.objects.create(Name = username, Amount=amount, Email=email)
        donation.save()
        return render(request,'master/razorpaygateway.html',{})

def paynext(request):
    context = {}
    if request.method == 'POST':
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        email = request.POST.get('email')
        amount = int(request.POST.get('amount'))
        x=Donation.objects.create(Name = name, Mobileno = phone, Email = email, Amount = amount)
        x.save()
        amount=amount*100
        order_amount = amount
        order_currency = 'INR'
        order_receipt = 'order_rcptid_11'
        notes = {'Shipping address': 'Bommanahalli, Bangalore'}
        client = razorpay.Client(auth=("rzp_live_T029oczISLBkmx", "hnEDgqWj3jOiHqOZfcksiVRG"))
        response = client.order.create(dict(amount = order_amount, currency = order_currency, receipt = order_receipt, notes = notes, payment_capture = '0'))
        order_id = response['id']
        order_status = response['status']
        if order_status=='created':
            context['price'] = order_amount/100
            context['name'] = name
            context['phone'] = phone
            context['email'] = email
            context['order_id'] = order_id
            transaction = Transaction.objects.create(made_by = name, amount = order_amount, order_id = order_id)
            transaction.save()
            return render(request, 'master/confirm_order.html', context)
    return HttpResponse('<h1>Error in  create order function</h1>')

def paynow(request):
    return render(request,'master/paynow.html')

def directpaygateway(request):
    if request.method == "GET":
        return render(request, 'dp.html')
    else:
        username = request.POST['name']
        mobileno = request.POST['phone']
        email = request.POST['email']
        amount = int(request.POST['amount'])
        x=Donation.objects.create(Name = username, Mobileno = mobileno, Email = email, Amount = amount)
        x.save()
        order_id=username+str(amount)+"dpscan_rt_spl"
        transaction = Transaction.objects.create(made_by = username, amount = amount, order_id = order_id)
        transaction.save()
        return render(request,'master/scan.html',{'amount':amount})

def finalscan(request):
    return render(request,'master/scan.html')

def about(request):
    return render(request,'master/about.html')

def suman(request):
    return render(request,'master/suman.html')

def bhanu(request):
    return render(request,'master/bhanu.html')

def testimony(request):
    return render(request,'master/testimony.html')

def feedback(request):
    if request.method == "POST":
        fm = feedbackform(request.POST,request.FILES)
        if fm.is_valid():
            x = fm.cleaned_data['Email']
            fm.save()
            return render(request,'master/thank.html')
        else:
            fm = feedbackform()
            return render(request,'master/feedback.html',{'fm':fm})
    else:
        fm = feedbackform()
        return render(request,'master/feedback.html',{'fm':fm})

def support(request):
    return render(request,'master/support.html')

def privacy(request):
    return render(request,'master/privacy.html')

def policy(request):
    return render(request,'master/policy.html')

def career(request):
    return render(request,'master/career.html')

def job(request):
    fm = digitalform()
    return render(request,'master/job.html',{'fm':fm})

def careerform(request):
    if request.method == "POST":
        return render(request,'master/jobformsubmit.html')
    else:
        return render(request,'master/ok.html')

def joberror(request):
    return render(request,'master/joberror.html')

def pdf_view(request):
    try:
        return FileResponse(open('iimcalcutta_consultcounsel.pdf', 'rb'), content_type='application/pdf')
    except FileNotFoundError:
        return HttpResponse('file not found')

def mentordetails(request):
    return render(request,'master/mentordetails.html')

def freesession(request):
    if request.method == 'POST':
        name = request.POST.get('username')
        phone = request.POST.get('mobileno')
        email = request.POST.get('email')
        field = request.POST.get('field')
        doubt = request.POST.get('doubt')
        x=Freesession.objects.create(name = name, mobile = phone, email = email, field = field, doubt = doubt)
        x.save()
        return render(request,'master/thank.html')
    else:
        return render(request,'master/freesession.html')

def summer(request):
    form = internform(request.POST or None,request.FILES or None)
    if request.POST:
        if form.is_valid():
            name = form.cleaned_data.get("Name")
            mobile = form.cleaned_data.get("Mobile")
            email = form.cleaned_data.get("Email")
            degree = form.cleaned_data.get("Degree")
            cv = request.FILES['resume']
            checkbox1 = request.POST.get('check1')
            checkbox2 = request.POST.get('check2')
            print(name,mobile,email,degree,cv,checkbox1,checkbox2,type(checkbox1),type(checkbox2))
            if checkbox1 == "on":
                c1 = True
            else:
                c1 = False
            if checkbox2=="on":
                c2 = True
            else:
                c2 = False
            print(c1,c2)
            x=Internship.objects.create(name = name, email = email, mobile = mobile, field = degree, cv = cv, checkbox1 = c1, checkbox2 = c2)
            return render(request,'master/thank.html')
        else:
            print(form)
            return render(request,'master/ok.html')
    else:
        return render(request,'master/internship.html',{'fm':form})

class AdsView(View):
    def get(self, request, *args, **kwargs):
        line  =  "google.com, pub-0000000000000000, DIRECT, f08c47fec0942fa0"
        return HttpResponse(line)
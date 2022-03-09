from django.shortcuts import render
from django.conf import settings
from .Form import question_form,answer_form,feedbackform
from .Form import volunter_form,digitalform
from .models import Forum_table,Transaction,Donation,Primemember,Mentor,transcatid,course_info
from .models import hiring_mentor,coupon,free_sessionform,internship,Court,solution
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect,HttpResponse,FileResponse
from django.contrib import auth
from django.views.decorators.csrf import csrf_exempt
from django.core.mail import send_mail
import razorpay
from django.views import View

class AdsView(View):
    """Replace pub-0000000000000000 with your own publisher ID"""
    line  =  "google.com, pub-0000000000000000, DIRECT, f08c47fec0942fa0"
    def get(self, request, *args, **kwargs):
        return HttpResponse(line)



def home(request):
    return render(request,'home.html')

def found(request):
    return render(request,'found.html')


def donation(request):
    return render(request,'donation.html')

def donation_next(request):
    if request.method=="GET":
        return render(request,'key.html')
    else:
        username = request.POST['username']
        email = request.POST['email']
        amount = int(request.POST['amount'])
        donation = Donation.objects.create(Name=username, Amount=amount,Email=email)
        donation.save()
        send_mail(
            'counsultandcounsel',
            'Admin,A new donation has come.Please check',
            settings.EMAIL_HOST_USER,
            ['sumanpatra68@gmail.com',
            'bhanup997@gmail.com'],
            fail_silently=False)
        send_mail(
            'counsultandcounsel',
            'Thank you for donation.We will use your money for need people.You will get the picture or document as well as we will publish your photo in our site.',
            settings.EMAIL_HOST_USER,
            [email],
            fail_silently=False)
        return render(request,'key.html',{})

def paynext(request):
    context = {}
    if request.method == 'POST':
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        email = request.POST.get('email')
        amount = int(request.POST.get('amount'))
        x=Donation.objects.create(Name=name,Mobileno=phone,Email=email,Amount=amount)
        x.save()
        amount=amount*100
        order_amount = amount
        order_currency = 'INR'
        order_receipt = 'order_rcptid_11'
        notes = {'Shipping address': 'Bommanahalli, Bangalore'}
        client = razorpay.Client(auth=("rzp_live_T029oczISLBkmx", "hnEDgqWj3jOiHqOZfcksiVRG"))
        response = client.order.create(dict(amount=order_amount, currency=order_currency, receipt=order_receipt, notes=notes, payment_capture='0'))
        order_id = response['id']
        order_status = response['status']
        if order_status=='created':
            context['price'] = order_amount/100
            context['name'] = name
            context['phone'] = phone
            context['email'] = email
            context['order_id'] = order_id
            transaction = Transaction.objects.create(made_by=name, amount=order_amount,order_id=order_id)
            transaction.save()
            return render(request, 'confirm_order.html', context)
    return HttpResponse('<h1>Error in  create order function</h1>')

def ready(request):
    return render(request,'rd.html')

def scan(request):
    return render(request,'scan.html')

def directpayy(request):
    if request.method == "GET":
        return render(request, 'dp.html')
    else:
        username = request.POST['name']
        mobileno = request.POST['phone']
        email = request.POST['email']
        amount = int(request.POST['amount'])
        x=Donation.objects.create(Name=username,Mobileno=mobileno,Email=email,Amount=amount)
        x.save()
        order_id=username+str(plan)+"dpscan_rt_spl"
        transaction = Transaction.objects.create(made_by=username, amount=amount,order_id=order_id)
        transaction.save()
        send_mail(
        'counsultandcounsel',
            'Admin, A new prime member is added by Direct Pay. Please check.',
            settings.EMAIL_HOST_USER,
            ['sumanpatra68@gmail.com',
            'bhanup997@gmail.com'],
            fail_silently=False
            )
        return render(request,'scan.html',{'amount':amount})

def testimony(request):
    return render(request,'testimony.html')

def support(request):
    return render(request,'support.html')

def about(request):
    return render(request,'about.html')

def bhanu(request):
    return render(request,'bhanu.html')

def suman(request):
    return render(request,'suman.html')

def feedback(request):
    if request.method=="POST":
        fm=feedbackform(request.POST,request.FILES)
        if fm.is_valid():
            x=fm.cleaned_data['Email']
            fm.save()
            send_mail(
            'counsultandcounsel',
            'Thank you for your feedback.We will check and reach out soon.Have a bright future ahead.',
            settings.EMAIL_HOST_USER,
            [x],
            fail_silently=False)
            send_mail(
            'counsultandcounsel',
            'Admin,you received a new feedback.Please check',
            settings.EMAIL_HOST_USER,
            ['sumanpatra68@gmail.com',
            'bhanup997@gmail.com'],
            fail_silently=False)
            return render(request,'thank.html')
        else:
            fm=feedbackform()
            return render(request,'feedback.html',{'fm':fm})
    else:
            fm=feedbackform()
            return render(request,'feedback.html',{'fm':fm})

def under(request):
    return render(request,'mail.html')

def database(request):
    data=Mentor.objects.all()
    return render(request,'main.html',{'data':data})

def privacy(request):
    return render(request,'privacy.html')

def policy(request):
    return render(request,'policy.html')

def career(request):
    return render(request,'career.html')

def digital(request):
    fm=digitalform()
    return render(request,'digital.html',{'fm':fm})

def save(request):
    if request.method=="POST":
        send_mail(
        'counsultandcounsel',
            'Admin,A new job application has come',
            settings.EMAIL_HOST_USER,
            ['sumanpatra68@gmail.com',
            'bhanup997@gmail.com'],
            fail_silently=False
            )
        return render(request,'found.html')
    else:
        return render(request,'ok.html')

def ad(request):
    file1 = open('ads.txt','r')
    d = file1.read()
    file1.close()
    return render(request,'demo.html',{'d':d})

def customer(request):
    return render(request,'customer.html')

def hiring(request):
    return render(request,'hiring.html')

def mentor(request):
    return render(request,'option.html')

def art(request):
    return render(request,'art.html')

def dancer(request):
    return render(request,'dancer.html')

def music(request):
    return render(request,'music.html')

def professional(request):
    return render(request,'professional.html')

def others(request):
    return render(request,'others.html')

def vlogger(request):
    return render(request,'vlogger.html')

def fashion(request):
    return render(request,'fashion.html')

def education(request):
    return render(request,'education.html')

def fitness(request):
    return render(request,'fitness.html')

def sports(request):
    return render(request,'sports.html')

def short(request):
    return render(request,'short.html')



def hireme(request):
    return render(request,'hire_home.html')

def mentordetails(request):
    return render(request,'mentordetails.html')

def form_submit(request):
    if request.method == 'POST':
        fname = request.POST.get('fname')
        email = request.POST.get('lname')
        phone = request.POST.get('phone')
        area = request.POST.get('area')
        x=hiring_mentor.objects.create(name=fname,email=email,area=area,mobile=phone)
        x.save()
        send_mail(
            'counsultandcounsel',
            'Admin,A new hiring request has come, Please check',
            settings.EMAIL_HOST_USER,
            ['sumanpatra68@gmail.com',
            'bhanup997@gmail.com'],
            fail_silently=False
            )
        return render(request,'hirementor.html')
    else:
        return render(request,'ok.html')


def pdf_view(request):
    try:
        return FileResponse(open('iimcalcutta_consultcounsel.pdf', 'rb'), content_type='application/pdf')
    except FileNotFoundError:
        return HttpResponse('file not found')

def couupon(request):
    if request.method == 'POST':
        name = request.POST.get('name_generated')
        mobile= request.POST.get('mobileno_generated')
        cp=name+"58"+mobile[7:9]
        x=coupon.objects.create(email=name,mobile=mobile,finalcoupon=cp)
        x.save()
        send_mail(
            'counsultandcounsel',
            'Admin,A new coupon request has come, Please check',
            settings.EMAIL_HOST_USER,
            ['sumanpatra68@gmail.com',
            'bhanup997@gmail.com'],
            fail_silently=False
            )
        return render(request,'newcoupon.html',{'coupon':cp})
    else:
        return render(request,'ok.html')

def okfoundation(request):
    return HttpResponseRedirect('https://m.facebook.com/Odisha-Kolkata-Foundation-107951754281024/?tsid=0.6352432790500597&source=result')

def freesession(request):
    if request.method == 'POST':
        name = request.POST.get('username')
        phone = request.POST.get('mobileno')
        email = request.POST.get('email')
        field = request.POST.get('field')
        doubt = request.POST.get('doubt')
        x=free_sessionform.objects.create(name=name,mobile=phone,email=email,field=field,doubt=doubt)
        x.save()
        send_mail(
            'counsultandcounsel',
            'Admin,A new free demo request has come, Please check',
            settings.EMAIL_HOST_USER,
            ['sumanpatra68@gmail.com',
            'bhanup997@gmail.com'],
            fail_silently=False
            )
        return render(request,'thank.html')
    else:
        return render(request,'pay.html')

def inter(request):
    if request.method == 'POST':
        name = request.POST.get('username')
        phone = request.POST.get('mobileno')
        email = request.POST.get('email')
        field = request.POST.get('cars')
        cv = request.POST.get('filename')
        x=internship.objects.create(name=name,mobile=phone,email=email,field=field,cv=cv)
        x.save()
        send_mail(
            'counsultandcounsel',
            'Admin,A new internship request has come, Please check',
            settings.EMAIL_HOST_USER,
            ['sumanpatra68@gmail.com',
            'bhanup997@gmail.com'],
            fail_silently=False
            )
        return render(request,'thank.html')
    else:
        return render(request,'offer.html')


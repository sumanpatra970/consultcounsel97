from django.shortcuts import render
from django.core.mail import send_mail
from career import settings
from django.contrib import auth
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponseRedirect,HttpResponse
from .Form import question_form,answer_form,volunter_form
import razorpay
from .models import Forum,Primemember,Transaction,Transcatid,Course,Court,Solution,Hirementor

def discussion(request):
    obj = Forum.objects.all()
    fm = question_form()
    return render(request,'master/discussion.html',{'v':obj,'form':fm})

def reply(request,id):
    if request.method == "POST":
        new = answer_form(request.POST)
        if new.is_valid():
            st = new.cleaned_data['answer']
            y = answer_form()
            v = Forum.objects.get(pk=id)
            v.answer = st
            v.save()
            t = v.question
            o = v.answer
            return render(request,'master/forum.html',{'o':o,'t':t,'fm':y,'g':id})
    else:
        v = Forum.objects.get(pk=id)
        t = v.question
        o = v.answer
        y = answer_form()
        return render(request,'master/forum.html',{'o':o,'t':t,'fm':y,'g':id})

def redirect(request):
    if request.method == "POST":
        y = question_form(request.POST)
        if y.is_valid():
            y.save()
            return HttpResponseRedirect('/discussion')
        else:
            return HttpResponseRedirect('/discussion')
    else:
        return HttpResponseRedirect('/discussion')

def session(request):
    return render(request,'master/session.html')

def step1(request):
        return render(request,'master/step1.html')

def step2(request):
    return render(request,'master/step2.html')

def step3(request):
    if request.user.is_authenticated:
        return render(request,'master/step3.html')
    else:
        return HttpResponseRedirect('login')

def nextpay(request):
    return HttpResponseRedirect('underconstruction')
    if request.method == "GET":
        return render(request, 'pay.html')
    else:
        username = request.POST['username']
        mobileno = request.POST['mobileno']
        email = request.POST['email']
        plan = int(request.POST['plan'])
        x=Primemember.objects.create(Name=username,Mobileno=mobileno,Email=email,Plan=plan)
        x.save()
    if plan==1:
        transaction = Transaction.objects.create(made_by=username, amount=150)
        transaction.save()
    elif plan==2:
        transaction = Transaction.objects.create(made_by=username, amount=400)
        transaction.save()
    elif plan==3:
        transaction = Transaction.objects.create(made_by=username, amount=800)
        transaction.save()
    else:
        transaction = Transaction.objects.create(made_by=username, amount=plan)
        transaction.save()

    PAYTM_SECRET_KEY = 'Ielms1FV!gmIm8Uv'
    merchant_key = PAYTM_SECRET_KEY
    PAYTM_MERCHANT_ID = 'JEYLdX59445091837751'
    PAYTM_WEBSITE = 'WEBSTAGING'
    PAYTM_CHANNEL_ID = 'WEB'
    PAYTM_INDUSTRY_TYPE_ID = 'Retail'
    params = (
        ('MID', PAYTM_MERCHANT_ID),
        ('ORDER_ID', str(transaction.order_id)),
        ('CUST_ID', str(transaction.made_by)),
        ('TXN_AMOUNT', str(transaction.amount)),
        ('CHANNEL_ID', PAYTM_CHANNEL_ID),
        ('WEBSITE', PAYTM_WEBSITE),
        ('INDUSTRY_TYPE_ID', PAYTM_INDUSTRY_TYPE_ID),
        ('CALLBACK_URL', 'http://insightlife.pythonanywhere.com/callback'),
    )

    paytm_params = dict(params)
    checksum = PaytmChecksum.generate_checksum(paytm_params, merchant_key)
    transaction.checksum = checksum
    transaction.save()
    paytm_params['CHECKSUMHASH'] = checksum
    print('SENT: ', checksum)
    return render(request, 'redirectt.html', context=paytm_params)

@csrf_exempt
def callback(request):
        if request.method == 'POST':
            received_data = dict(request.POST)
            paytm_params = {}
            paytm_checksum = received_data['CHECKSUMHASH'][0]
            for key, value in received_data.items():
                if key == 'CHECKSUMHASH':
                    paytm_checksum = value[0]
                else:
                    paytm_params[key] = str(value[0])
            PAYTM_SECRET_KEY = 'Ielms1FV!gmIm8Uv'
            is_valid_checksum = PaytmChecksum.verify_checksum(paytm_params, PAYTM_SECRET_KEY, str(paytm_checksum))
            if is_valid_checksum:
                received_data['message'] = "Checksum Matched"
                return render(request, 'master/callback.html', context=received_data)
            else:
                received_data['message'] = "Checksum Mismatched"
                return render(request, 'master/callback.html', context=received_data)
        else:
            return  render(request,'master/ok.html')

def underconstruction(request):
    return render(request,'master/uc.html')

def directpay(request):
    name = request.user
    return render(request,'master/directpay.html',{'name':name,'request':request})

def qrdirect(request):
    if request.method == "GET":
        return render(request, 'master/directpay.html')
    else:
        username = request.POST['name']
        mobileno = request.POST['phone']
        email = request.POST['email']
        plan = int(request.POST['plan'])
        refer = request.POST['refer']
        concern = request.POST['concern']
        if plan == 1:
            Amount = 150
        elif plan == 2:
            Amount = 300
        else:
            Amount = 400
        x = Primemember.objects.create(Name = username, Mobileno = mobileno, Email = email, Plan = plan, Refered = refer, Query = concern)
        x.save()
        order_id = username+str(plan)+"dpscan_rt_spl"
        transaction = Transaction.objects.create(made_by=username, amount=Amount,order_id=order_id)
        transaction.save()
        return render(request,'master/scan.html',{'amount':Amount})
    
def razorpaygate(request):
    return render(request, 'master/razorpay.html', {})

def create_order(request):
    context = {}
    if request.method == 'POST':
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        email = request.POST.get('email')
        product = request.POST.get('plan')
        refer = request.POST.get('refer')
        concern = request.POST['concern']
        x = Primemember.objects.create(Name = name, Mobileno = phone, Email = email, Plan = product, Refered = refer, Query = concern)
        x.save()
        order_amount = 100
        if product == "1":
            order_amount = 15000
        elif product == '2':
            order_amount = 30000
        elif product == '3':
            order_amount = 40000
        order_currency = 'INR'
        order_receipt = 'order_rcptid_11'
        notes = {'Shipping address': 'Bommanahalli, Bangalore'}
        client = razorpay.Client(auth=("rzp_live_T029oczISLBkmx", "hnEDgqWj3jOiHqOZfcksiVRG"))
        response = client.order.create(dict(amount=order_amount, currency=order_currency, receipt=order_receipt, notes=notes, payment_capture='0'))
        order_id = response['id']
        order_status = response['status']
        if order_status=='created':
            context['product_id'] = product
            context['price'] = order_amount/100
            context['name'] = name
            context['phone'] = phone
            context['email'] = email
            context['order_id'] = order_id
            transaction = Transaction.objects.create(made_by=name, amount=order_amount,order_id=order_id)
            transaction.save()
            return render(request, 'master/confirm_order.html', context)
    return HttpResponse('<h1>Error in  create order function</h1>')

def payment_status(request):
    response = request.POST
    client = razorpay.Client(auth = ("rzp_live_T029oczISLBkmx", "hnEDgqWj3jOiHqOZfcksiVRG"))
    params_dict = {
        'razorpay_payment_id' : response['razorpay_payment_id'],
        'razorpay_order_id' : response['razorpay_order_id'],
        'razorpay_signature' : response['razorpay_signature']
    }
    x = response['razorpay_payment_id']
    y = response['razorpay_order_id']
    v = Transcatid.objects.create(order_id = y, transcation_id = x)
    v.save()
    try:
        status = client.utility.verify_payment_signature(params_dict)
        return render(request, 'master/order_summary.html', {'status': 'Payment Successful','x':x,'y':y})
    except:
        return render(request, 'master/order_summary.html', {'status': 'Payment Faliure!!!'})

def mentor(request):
    return render(request,'master/mentor.html')

def mentorform(request):
    if request.method == "POST":
        fm = volunter_form(request.POST,request.FILES)
        if fm.is_valid():
            email = fm.cleaned_data['Email']
            fm.save()
            return render(request,'master/mentor-form.html')
        else:
            fm = volunter_form()
            return render(request,'master/mentorform.html',{'fm':fm})
    else:
        fm = volunter_form()
        return render(request,'master/mentorform.html',{'fm':fm})

def startcourse(request):
    return render(request,'master/fillup.html')

def hrcourse(request):
    return render(request,'master/hrcourse.html')

def skilldevelopment(request):
    return render(request,'master/skilldevelopment.html')

def software(request):
    return render(request,'master/software.html')

def courseform(request):
    return render(request,'master/courseform.html')

def paydirect(request):
    if request.method == 'POST':
        fname = request.POST.get('fname')
        lname= request.POST.get('lname')
        phone = request.POST.get('mobile')
        email = request.POST.get('email')
        refered = request.POST.get('emaill')
        x = Course.objects.create(name = fname+lname, email = email, mobile = phone, Refered = refered)
        x.save()
        return render(request,'master/scan.html')

def virtualcourt(request):
    return render(request,'master/virtualcourt.html')

def bookcourt(request):
    return render(request,'master/bookcourt.html')

def courtform(request):
    return render(request,'master/courtform.html')

def courtformsubmit(request):
    if request.method == 'POST':
        fname = request.POST.get('lastname')
        location = request.POST.get('location')
        phone = request.POST.get('mobile')
        email = request.POST.get('email')
        x = Court.objects.create(name = fname, mobile = phone, email = email, location = location)
        x.save()
    return render(request,'master/courtformsubmit.html')

def itsolution(request):
    return render(request,'master/itsolution.html')

def itsolutionrequest(request):
    if request.method == 'POST':
        name = request.POST.get('username')
        phone = request.POST.get('mobileno')
        email = request.POST.get('email')
        x = Solution.objects.create(name = name, mobile = phone, email = email)
        x.save()
        return render(request,'master/thank.html')
    else:
        return render(request,'master/solution.html')

def hireme(request):
    return render(request,'master/hireme.html')

def hiringform(request):
    if request.method == 'POST':
        fname = request.POST.get('fname')
        email = request.POST.get('lname')
        phone = request.POST.get('phone')
        area = request.POST.get('area')
        x = Hirementor.objects.create(name = fname, email = email, area = area, mobile = phone)
        x.save()
        return render(request,'master/hiringform.html')
    else:
        return render(request,'master/ok.html')

def freetraining(request):
    if request.method == 'POST':
        name = request.POST.get('username')
        phone = request.POST.get('mobileno')
        email = request.POST.get('email')
        x = Solution.objects.create(name = name, mobile = phone, email = email)
        x.save()
        return render(request,'master/thank.html')
    else:
        return render(request,'master/freetraining.html')
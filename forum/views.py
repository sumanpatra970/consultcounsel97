from django.shortcuts import render
from django.conf import settings
from .Form import question_form,answer_form,account_creation_form,feedbackform
from .Form import login_form,name_form,password_form,user_change_form,volunter_form,digitalform
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

def signup(request):
    if request.method=="POST":
        fm=account_creation_form(request.POST)
        if fm.is_valid():
            email=fm.cleaned_data['email']
            fm.save()
            send_mail(
            'counsultandcounsel',
            'Admin,A new member is added by signup, Please check',
            settings.EMAIL_HOST_USER,
            ['sumanpatra68@gmail.com',
            'bhanup997@gmail.com'],
            fail_silently=False
            )
            send_mail(
            'counsultandcounsel',
            'Thank you for becoming our memeber.We bring you the best consulting and counselling services irrespective of field with the help of renowned professionals in that particular concerned area... We have forum section in which you can put up your question relating to any domain which will be answered by our highly trained mentors in the above said domain for FREE.You can avail best of our services by becoming premium member and avail the facilities provided by us via proficient trainers in a meagre amount. Please feel free to reach out to us or visit www.consultandcounsel.com',
            settings.EMAIL_HOST_USER,
            [email],
            fail_silently=False)
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

def discussion(request):
    obj=Forum_table.objects.all()
    fm=question_form()
    return render(request,'discussion.html',{'v':obj,'form':fm})

def reply(request,id):
    if request.method=="POST":
        new=answer_form(request.POST)
        if new.is_valid():
            st=new.cleaned_data['answer']
            y=answer_form()
            v=Forum_table.objects.get(pk=id)
            v.answer=st;
            v.save()
            t=v.question
            o=v.answer
            return render(request,'forum.html',{'o':o,'t':t,'fm':y,'g':id})
    else:
        v=Forum_table.objects.get(pk=id)
        t=v.question
        o=v.answer
        y=answer_form()
        return render(request,'forum.html',{'o':o,'t':t,'fm':y,'g':id})

def redirect(request):
    if request.method=="POST":
        y=question_form(request.POST)
        if y.is_valid():
            y.save()
            return HttpResponseRedirect('/discussion')
        else:
            return HttpResponseRedirect('/discussion')
    else:
            return HttpResponseRedirect('/discussion')

def session(request):
    return render(request,'session.html')

def prime(request):
        return render(request,'planchoice.html')

def plan(request):
    return render(request,'planchoicenext.html')

def plan_next(request):
    if request.user.is_authenticated:
        return render(request,'payment.html')
    else:
        return HttpResponseRedirect('login')

def paytm(request):
    return render(request,'planchoice.html')

def nextpay(request):
    return HttpResponseRedirect('underconst')
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
                send_mail(
                'counsultandcounsel',
                'ADMIN,A new prime member is added.Please check and acknowledge.Thank you.',
                settings.EMAIL_HOST_USER,
                ['sumanpatra68@gmail.com',
                'bhanup997@gmail.com'],
                fail_silently=False)
                return render(request, 'callback.html', context=received_data)
            else:
                received_data['message'] = "Checksum Mismatched"
                return render(request, 'callback.html', context=received_data)
        else:
            return  render(request,'ok.html')

def testing(request):
    return render(request, 'order.html', {})

def create_order(request):
    context = {}
    if request.method == 'POST':
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        email = request.POST.get('email')
        product = request.POST.get('plan')
        refer = request.POST.get('refer')
        concern= request.POST['concern']
        x=Primemember.objects.create(Name=name,Mobileno=phone,Email=email,Plan=product,Refered=refer,Query=concern)
        x.save()
        order_amount = 100
        if product == "1":
            order_amount = 15000
        elif product == '2':
            order_amount = 30000
        elif product == '3':
            order_amount = 40000
        else:
            order_amount=10000
        order_currency = 'INR'
        order_receipt = 'order_rcptid_11'
        notes = {'Shipping address': 'Bommanahalli, Bangalore'}
        client = razorpay.Client(auth=("rzp_live_T029oczISLBkmx", "hnEDgqWj3jOiHqOZfcksiVRG"))
        response = client.order.create(dict(amount=order_amount/100, currency=order_currency, receipt=order_receipt, notes=notes, payment_capture='0'))
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
            return render(request, 'confirm_order.html', context)
    return HttpResponse('<h1>Error in  create order function</h1>')

def payment_status(request):
    response = request.POST
    client = razorpay.Client(auth=("rzp_live_T029oczISLBkmx", "hnEDgqWj3jOiHqOZfcksiVRG"))
    params_dict = {
        'razorpay_payment_id' : response['razorpay_payment_id'],
        'razorpay_order_id' : response['razorpay_order_id'],
        'razorpay_signature' : response['razorpay_signature']
    }
    x=response['razorpay_payment_id']
    y=response['razorpay_order_id']
    v=transcatid.objects.create(order_id=y,transcation_id=x)
    v.save()
    send_mail(
        'counsultandcounsel',
            'Admin,A new prime member is added.Please check. Thank you.',
            settings.EMAIL_HOST_USER,
            ['sumanpatra68@gmail.com',
            'bhanup997@gmail.com'],
            fail_silently=False
            )
    try:
        status = client.utility.verify_payment_signature(params_dict)
        return render(request, 'order_summary.html', {'status': 'Payment Successful','x':x,'y':y})
    except:
        return render(request, 'order_summary.html', {'status': 'Payment Faliure!!!'})

def directpay(request):
    name=request.user
    return render(request,'directpay.html',{'name':name,'request':request})

def direct(request):
    if request.method == "GET":
        return render(request, 'directpay.html')
    else:
        username = request.POST['name']
        mobileno = request.POST['phone']
        email = request.POST['email']
        plan = int(request.POST['plan'])
        refer = request.POST['refer']
        concern= request.POST['concern']
        if plan==1:
            Amount=150
        elif plan==2:
            Amount=300
        else:
            Amount=400
        x=Primemember.objects.create(Name=username,Mobileno=mobileno,Email=email,Plan=plan,Refered=refer,Query=concern)
        x.save()
        order_id=username+str(plan)+"dpscan_rt_spl"
        transaction = Transaction.objects.create(made_by=username, amount=Amount,order_id=order_id)
        transaction.save()
        send_mail(
        'counsultandcounsel',
            'Admin, A new prime member is added by Direct Pay. Please check.',
            settings.EMAIL_HOST_USER,
            ['sumanpatra68@gmail.com',
            'bhanup997@gmail.com'],
            fail_silently=False
            )
        return render(request,'scan.html',{'amount':Amount})

def netbanking(request):
    return HttpResponseRedirect('/paymentstart')

def volunter(request):
    return render(request,'volunter.html')

def volunter_next(request):
    if request.method=="POST":
        fm=volunter_form(request.POST,request.FILES)
        if fm.is_valid():
            email=fm.cleaned_data['Email']
            fm.save()
            send_mail(
            'counsultandcounsel',
            'Admin,A new mentor has been registered.Please check.',
            settings.EMAIL_HOST_USER,
            ['sumanpatra68@gmail.com',
            'bhanup997@gmail.com'],
            fail_silently=False)
            send_mail(
            'counsultandcounsel',
            'Thank you for becoming a mentor.You will get call by our team.We are growing and we want you to grow as well as. Guide students by taking session and earn.',
            settings.EMAIL_HOST_USER,
            [email],
            fail_silently=False)
            return render(request,'volunternext.html')
        else:
            fm=volunter_form()
            return render(request,'volunterform.html',{'fm':fm})
    else:
        fm=volunter_form()
        return render(request,'volunterform.html',{'fm':fm})

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
        x=Donation.objects.create(Name=username,Mobileno=mobileno,Email=email,Amount=amount,Date="22.02")
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

def rahul(request):
    return render(request,'rahul.html')

def radhakant(request):
    return render(request,'radhakant.html')

def abhijit(request):
    return render(request,'abhijit.html')

def kavitha(request):
    return render(request,'kavitha.html')

def nivi(request):
    return render(request,'nivi.html')

def shashank(request):
    return render(request,'shashank.html')

def jyoti(request):
    return render(request,'jyoti.html')

def sumant(request):
    return render(request,'sumant.html')

def juned(request):
    return render(request,'juned.html')

def soni(request):
    return render(request,'soni.html')

def koushik(request):
    return render(request,'koushik.html')

def pragati(request):
    return render(request,'pragati.html')

def karan(request):
    return render(request,'karan.html')

def bikram(request):
    return render(request,'bikram.html')

def goutam(request):
    return render(request,'goutam.html')

def shuv(request):
    return render(request,'shuv.html')

def shradha(request):
    return render(request,'shradha.html')

def popin(request):
    return render(request,'popin.html')

def loops(request):
    return render(request,'loops.html')

def damini(request):
    return render(request,'damini.html')

def sujata(request):
    return render(request,'sujata.html')

def aayusi(request):
    return render(request,'aayushi.html')

def sukesh(request):
    return render(request,'sukesh.html')

def shree(request):
    return render(request,'shree.html')

def piyush(request):
    return render(request,'prityush.html')

def priyanka(request):
    return render(request,'priyanka.html')

def ahana(request):
    return render(request,'ahana.html')

def rispa(request):
    return render(request,'rispa.html')

def jawat(request):
    return render(request,'jawat.html')

def manan(request):
    return render(request,'manan.html')

def swapansu(request):
    return render(request,'sapansu.html')

def srimaa(request):
    return render(request,'srimaa.html')

def abhya(request):
    return render(request,'abhya.html')

def anupam(request):
    return render(request,'anupam.html')

def anindya(request):
    return render(request,'anindya.html')

def krutee(request):
    return render(request,'krutee.html')

def sandhya(request):
    return render(request,'sandhya.html')

def tejaswi(request):
    return render(request,'tejaswi.html')

def farheen(request):
    return render(request,'farheen.html')

def darshini(request):
    return render(request,'darshini.html')

def jita(request):
    return render(request,'jita.html')

def smita(request):
    return render(request,'smita.html')

def sanjana(request):
    return render(request,'sanjana.html')

def padmini(request):
    return render(request,'padmini.html')

def saloni(request):
    return render(request,'saloni.html')

def soumya(request):
    return render(request,'soumya.html')

def abhinash(request):
    return render(request,'abhinash.html')

def hardeek(request):
    return render(request,'hardeek.html')

def deekshith(request):
    return render(request,'deekshith.html')

def bharatendu(request):
    return render(request,'bharatendu.html')

def animesh(request):
    return render(request,'animesh.html')

def abhipsa(request):
    return render(request,'abhipsa.html')

def ajay(request):
    return render(request,'ajay.html')

def amit_patjoshi(request):
    return render(request,'amit_patjoshi.html')

def richa(request):
    return render(request,'richa.html')

def priynka_br(request):
    return render(request,'priynka_br.html')

def soumya_prusti(request):
    return render(request,'soumya_prusti.html')

def tikeshwar(request):
    return render(request,'tikeshwar.html')

def pallavi(request):
    return render(request,'pallavi.html')

def sidhi(request):
    return render(request,'sidhi.html')

def soumav(request):
    return render(request,'soumav.html')

def soumyashree(request):
    return render(request,'soumyashree.html')

def asd(request):
    return render(request,'asd.html')

def prachi(request):
    return render(request,'prachi.html')

def sushree(request):
    return render(request,'sushree.html')

def pallavii(request):
    return render(request,'pallavii.html')

def ayushi(request):
    return render(request,'ayushi.html')

def ayush(request):
    return render(request,'ayush.html')

def anukta(request):
    return render(request,'anukta.html')

def ssn(request):
    return render(request,'ssn.html')

def nirali(request):
    return render(request,'nirali.html')

def deeja(request):
    return render(request,'deeja.html')

def deepa(request):
    return render(request,'deepa.html')

def pp(request):
    return render(request,'pp.html')

def chetna(request):
    return render(request,'chetna.html')

def adityoli(request):
    return render(request,'adityaoli.html')

def prasanna(request):
    return render(request,'prasanna.html')

def albin(request):
    return render(request,'albin.html')

def subashis(request):
    return render(request,'subashis.html')

def nikhil(request):
    return render(request,'nikhil.html')

def asmita(request):
    return render(request,'asmita.html')

def trilochan(request):
    return render(request,'trilochan.html')

def jayesh(request):
    return render(request,'jayesh.html')

def saswat(request):
    return render(request,'saswat.html')

def rishi(request):
    return render(request,'rishi.html')

def manisha(request):
    return render(request,'manisha.html')

def rudra(request):
    return render(request,'demo.html')

def somensoni(request):
    return render(request,'notfound.html')

def tannya(request):
    return render(request,'tannya.html')

def pooja(request):
    return render(request,'pooja.html')

def haritha(request):
    return render(request,'haritha.html')

def gangaprasad(request):
    return render(request,'ganga.html')

def amal(request):
    return render(request,'amal.html')

def oshi(request):
    return render(request,'oshi.html')

def lipsaa(request):
    return render(request,'lipsaa.html')

def anand(request):
    return render(request,'anand.html')

def werika(request):
    return render(request,'werika.html')

def smaroki(request):
    return render(request,'smaroki.html')

def sanju(request):
    return render(request,'sanju.html')

def bvaditya(request):
    return render(request,'bvaditya.html')

def srivalli(request):
    return render(request,'svp.html')

def ritu(request):
    return render(request,'ritu.html')

def chiranjeeb(request):
    return render(request,'chiranjeeb.html')

def boaz(request):
    return render(request,'boaz.html')

def rahul2(request):
    return render(request,'rahull.html')

def apruba(request):
    return render(request,'apruba.html')

def nimai(request):
    return render(request,'nimai.html')

def sarthak(request):
    return render(request,'sarthak.html')

def suniti(request):
    return render(request,'suniti.html')

def sushil(request):
    return render(request,'sushil.html')

def sushant(request):
    return render(request,'sushant.html')

def raju(request):
    return render(request,'raju.html')

def shruti(request):
    return render(request,'shruti.html')

def sambit(request):
    return render(request,'sambit.html')

def rashmi(request):
    return render(request,'rashmi.html')

def utkal(request):
    return render(request,'utkal.html')

def akanshya(request):
    return render(request,'akanshya.html')

def course(request):
    return render(request,'course.html')

def skill(request):
    return render(request,'skilldevelopment.html')

def software(request):
    return render(request,'software.html')

def paydirect(request):
    if request.method == 'POST':
        fname = request.POST.get('fname')
        lname= request.POST.get('lname')
        phone = request.POST.get('phone')
        email = request.POST.get('email')
        refered=request.POST.get('emaill')
        x=course_info.objects.create(name=fname+lname,email=email,Refered=refered,mobile=phone)
        x.save()
        send_mail(
            'counsultandcounsel',
            'Admin,you received a new course request.Please check',
            settings.EMAIL_HOST_USER,
            ['sumanpatra68@gmail.com',
            'bhanup997@gmail.com'],
            fail_silently=False)
        return render(request,'scan.html')

def fillup(request):
    return render(request,'fillup.html')

def qrp(request):
    return render(request,'form.html')

def manasasu(request):
    return render(request,'manasasu.html')

def jayshree(request):
    return render(request,'jayshree.html')

def shuvransu(request):
    return render(request,'sutripathy.html')

def chetana(request):
    return render(request,'chetana_mike.html')

def mrvish(request):
    return render(request,'mrvish.html')

def aman(request):
    return render(request,'aman.html')

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

def indu(request):
    return render(request,'indu.html')

def swaraj(request):
    return render(request,'swaraj.html')

def swadesh(request):
    return render(request,'swadesh.html')

def kavya(request):
    return render(request,'kavya.html')

def shilky(request):
    return render(request,'shilky.html')

def radha(request):
    return render(request,'radha.html')

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

def virtualcourt(request):
    return render(request,'virtualcourt.html')

def bookcourt(request):
    return render(request,'booking.html')

def booklast(request):
    return render(request,'bookcourtroom.html')

def lastonly(request):
    if request.method == 'POST':
        fname = request.POST.get('lastname')
        location = request.POST.get('location')
        phone = request.POST.get('mobile')
        email = request.POST.get('email')
        x=Court.objects.create(name=fname,mobile=phone,email=email,location=location)
        x.save()
        send_mail(
            'counsultandcounsel',
            'Admin,A new courthiring request has come, Please check',
            settings.EMAIL_HOST_USER,
            ['sumanpatra68@gmail.com',
            'bhanup997@gmail.com'],
            fail_silently=False
            )
    return render(request,'lastcall.html')

def itsolution(request):
    return render(request,'itsolution.html')

def booksession(request):
    if request.method == 'POST':
        name = request.POST.get('username')
        phone = request.POST.get('mobileno')
        email = request.POST.get('email')
        x=solution.objects.create(name=name,mobile=phone,email=email)
        x.save()
        send_mail(
            'counsultandcounsel',
            'Admin,A new project request has come, Please check',
            settings.EMAIL_HOST_USER,
            ['sumanpatra68@gmail.com',
            'bhanup997@gmail.com'],
            fail_silently=False
            )
        return render(request,'thank.html')
    else:
        return render(request,'solution.html')

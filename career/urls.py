from django.contrib import admin
from django.urls import path
from forum import  views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.views.generic.base import RedirectView
from django.contrib.staticfiles.storage import staticfiles_storage

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home),
    path('signup',views.signup),
    path('account',views.account),
    path('login',views.login),
    path('editprofile',views.editaccount),
    path('password',views.password),
    path('passwordchange',views.passwordchange),
    path('logout',views.logout),
    path('discussion',views.discussion),
    path('reply/<int:id>/',views.reply),
    path('redirect',views.redirect),
    path('session',views.session),
    path('prime',views.prime),
    path('step2',views.plan),
    path('step3',views.plan_next),
    path('nextpay',views.nextpay),
    path('paytm',views.paytm),
    path('callback',views.callback),
    path('directpay',views.directpay),
    path('qr',views.direct),
    path('netbanking',views.netbanking),
    path('paymentstart', views.testing),
    path('confirm_order', views.create_order),
    path('payment_status', views.payment_status,name = 'payment_status'),
    path('volunter',views.volunter),
    path('mentor',views.volunter_next),
    path('donation',views.donation),
    path('donation_next',views.donation_next),
    path('paynext',views.paynext),
    path('gonow',views.ready),
    path('directpayy',views.directpayy),
    path('finalscan',views.scan),
    path('about',views.about),
    path('read/suman',views.suman),
    path('read/bhanu',views.bhanu),
    path('testimony',views.testimony),
    path('feedback',views.feedback),
    path('support',views.support),
    path('found',views.found),
    path('career',views.career),
    path('CC001',views.digital),
    path('save',views.save),
    path('CC002',views.customer),
    path('hiring',views.hiring),
    path('mentors',views.mentor),
    path('underconst',views.under),
    path('database',views.database),
    path('art',views.art),
    path('dancer',views.dancer),
    path('musician',views.music),
    path('professional',views.professional),
    path('others',views.others),
    path('vlogger',views.vlogger),
    path('fashion',views.fashion),
    path('education',views.education),
    path('fitness',views.fitness),
    path('sports',views.sports),
    path('privacy',views.privacy),
    path('policy',views.policy),
    path('shree',views.shree),
    path('rahul',views.rahul),
    path('jyoti',views.jyoti),
    path('shashank',views.shashank),
    path('abhijit',views.abhijit),
    path('radhakant',views.radhakant),
    path('kavitha',views.kavitha),
    path('Nivi',views.nivi),
    path('sumant',views.sumant),
    path('juned',views.juned),
    path('soni',views.soni),
    path('koushik',views.koushik),
    path('pragati',views.pragati),
    path('karan',views.karan),
    path('bikram',views.bikram),
    path('goutam',views.goutam),
    path('shuv',views.shuv),
    path('shradha',views.shradha),
    path('popin',views.popin),
    path('loops',views.loops),
    path('damini',views.damini),
    path('sujata',views.sujata),
    path('aayushi',views.aayusi),
    path('sukesh',views.sukesh),
    path('piyush',views.piyush),
    path('priyanka',views.priyanka),
    path('ahana',views.ahana),
    path('rispa',views.rispa),
    path('jawat',views.jawat),
    path('manan',views.manan),
    path('soumya',views.soumya),
    path('swopansu',views.swapansu),
    path('srimaa',views.srimaa),
    path('abhya',views.abhya),
    path('anupam',views.anupam),
    path('krutee',views.krutee),
    path('anindya',views.anindya),
    path('sandhya',views.sandhya),
    path('tejaswi',views.tejaswi),
    path('farheen',views.farheen),
    path('darshini',views.darshini),
    path('jita',views.jita),
    path('smita',views.smita),
    path('sanjana',views.sanjana),
    path('padmini',views.padmini),
    path('saloni',views.saloni),
    path('soumya',views.soumya),
    path('hardeek',views.hardeek),
    path('deekshith',views.deekshith),
    path('animesh',views.animesh),
    path('bharatendu',views.bharatendu),
    path('abhinash',views.abhinash),
    path('abhipsa',views.abhipsa),
    path('amit_patjoshi',views.amit_patjoshi),
    path('richa',views.richa),
    path('priynka_br',views.priynka_br),
    path('ajay',views.ajay),
    path('soumya_prusti',views.soumya_prusti),
    path('tikeshwar',views.tikeshwar),
    path('pallavi',views.pallavi),
    path('sidhi',views.sidhi),
    path('soumav',views.soumav),
    path('soumyashree',views.soumyashree),
    path('asd',views.asd),
    path('prachi',views.prachi),
    path('sushree',views.sushree),
    path('ayushi',views.ayushi),
    path('pallavii',views.pallavii),
    path('ayush',views.ayush),
    path('anukta',views.anukta),
    path('nirali',views.nirali),
    path('ssn',views.ssn),
    path('deepa',views.deepa),
    path('deeja',views.deeja),
    path('pp',views.pp),
    path('chetna',views.chetna),
    path('adityaoli',views.adityoli),
    path('prasanna',views.prasanna),
    path('albin',views.albin),
    path('subashis',views.subashis),
    path('nikhil',views.nikhil),
    path('jayesh',views.jayesh),
    path('asmita',views.asmita),
    path('trilochan',views.trilochan),
    path('saswat',views.saswat),
    path('manisha',views.manisha),
    path('rishi',views.rishi),
    path('rudra',views.rudra),
    path('somensoni',views.somensoni),
    path('tannya',views.tannya),
    path('pooja',views.pooja),
    path('haritha',views.haritha),
    path('gangaprasad',views.gangaprasad),
    path('amal',views.amal),
    path('oshi',views.oshi),
    path('anand',views.anand),
    path('lipsaa',views.lipsaa),
    path('sanju',views.sanju),
    path('smaroki',views.smaroki),
    path('werika',views.werika),
    path('bvaditya',views.bvaditya),
    path('srivalli',views.srivalli),
    path('ritu',views.ritu),
    path('chiranjeeb',views.chiranjeeb),
    path('boaz',views.boaz),
    path('apruba',views.apruba),
    path('rahul2',views.rahul2),
    path('nimai',views.nimai),
    path('sarthak',views.sarthak),
    path('sushil',views.sushil),
    path('sushant',views.sushant),
    path('suniti',views.suniti),
    path('raju',views.raju),
    path('shruti',views.shruti),
    path('sambit',views.sambit),
    path('rashmi',views.rashmi),
    path('utkal',views.utkal),
    path('akanshya',views.akanshya),
    path('course',views.course),
    path('skilldevelopment',views.skill),
    path('softwaretrain',views.software),
    path('paydirect',views.paydirect),
    path('startnow',views.fillup),
    path('qrp',views.qrp),
    path('manasasu',views.manasasu),
    path('jayshree',views.jayshree),
    path('shuvransu',views.shuvransu),
    path('chetana',views.chetana),
    path('mrvish',views.mrvish),
    path('aman',views.aman),
    path('indu',views.indu),
    path('swadesh',views.swadesh),
    path('swaraj',views.swaraj),
    path('kavya',views.kavya),
    path('shilky',views.shilky),
    path('hireme',views.hireme),
    path('iimcalcutta-project',views.pdf_view),
    path('mentordetails',views.mentordetails),
    path('form_submit',views.form_submit),
    path('couponavail',views.couupon),
    path('freesession',views.freesession),
    path('internship',views.inter),
    path('virtualcourt',views.virtualcourt),
    path('bookcourt',views.bookcourt),
    path('lastcall',views.booklast),
    path('calling',views.lastonly),
    path('radha',views.radha),
    path('itsolution',views.itsolution),
    path('digital',views.booksession),
     path(
        "ads.txt",
        RedirectView.as_view(url=staticfiles_storage.url("ads.txt")),
    ),
]

urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

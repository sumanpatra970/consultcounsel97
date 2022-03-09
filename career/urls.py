from django.contrib import admin
from django.urls import path,include
from forum import  views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.views.generic.base import RedirectView
from django.contrib.staticfiles.storage import staticfiles_storage

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home),
    path('',include('community.urls')),
    path('',include('account.urls')),
    path('',include('services.urls')),
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
    path('hireme',views.hireme),
    path('iimcalcutta-project',views.pdf_view),
    path('mentordetails',views.mentordetails),
    path('form_submit',views.form_submit),
    path('couponavail',views.couupon),
    path('freesession',views.freesession),
    path('internship',views.inter),
    path("ads.txt",RedirectView.as_view(url=staticfiles_storage.url("ads.txt")),),
]

urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

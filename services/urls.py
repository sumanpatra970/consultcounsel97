from django.urls import path
from . import views

urlpatterns = [
    path('discussion',views.discussion),
    path('reply/<int:id>/',views.reply),
    path('redirect',views.redirect),
    path('session',views.session),
    path('step1',views.step1),
    path('step2',views.step2),
    path('step3',views.step3),
    path('nextpay',views.nextpay),
    path('callback',views.callback),
    path('directpay',views.directpay),
    path('qr',views.qrdirect),
    path('razorpaygate', views.razorpaygate),
    path('confirm_order', views.create_order),
    path('payment_status', views.payment_status,
    name='payment_status'),
    path('join-as-mentor',views.mentor),
    path('mentor-form',views.mentorform),
    path('startnow',views.startcourse),
    path('hrcourse',views.hrcourse),
    path('skilldevelopment',views.skilldevelopment),
    path('softwarecourse',views.software),
    path('course-form',views.courseform),
    path('paydirect',views.paydirect),
    path('virtualcourt',views.virtualcourt),
    path('bookcourt',views.bookcourt),
    path('courtform',views.courtform),
    path('court-request-done',views.courtformsubmit),
    path('itsolution',views.itsolution),
    path('itsolution-request-form',views.itsolutionrequest),
    path('hireme',views.hireme),
    path('hiring-mentor-done',views.hiringform),
    path('underconstruction',views.underconstruction),
    path('freetraining',views.freetraining)
    ]
from django.urls import path
from . import views
urlpatterns = [
    path('signup',views.signup),
    path('account',views.account),
    path('login',views.login),
    path('editprofile',views.editaccount),
    path('password',views.password),
    path('passwordchange',views.passwordchange),
    path('logout',views.logout)]
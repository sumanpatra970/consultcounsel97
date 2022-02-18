from django.urls import path

from forum.views import AdsView

urlpatterns = [
    path('ads.txt', AdsView.as_view()),
]
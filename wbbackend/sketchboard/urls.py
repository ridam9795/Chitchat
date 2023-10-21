
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index.as_view(),name='index'),
    path('register/',views.Register.as_view(),name='register'),
    path('verify_otp/',views.VerifyOTP.as_view(),name='Verify Otp')
]

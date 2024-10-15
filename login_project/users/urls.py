from django.urls import path
from . import views
from django.shortcuts import render, redirect

urlpatterns = [
    path('', views.login_view, name='login'),
    path('register/', views.register_view, name='register'),
    path('dashboard/', views.dashboard_view, name='dashboard'),
    path('result/', views.result_view, name='result'),
]

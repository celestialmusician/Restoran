from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [

    path('',views.HomeView.as_view(),name='home'),

    path('about/',views.AboutView.as_view(),name='about'),

    path('menu/',views.MenuView.as_view(),name='menu'),

    path('contact/',views.ContactView.as_view(),name='contact'),

    path('booking/',views.BookingView.as_view(),name='booking'),

]
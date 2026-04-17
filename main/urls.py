from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="Home"),
    path('about-us/', views.about, name="aboutUs"),
    path('contact-us/', views.contact, name="contactUs"),
]
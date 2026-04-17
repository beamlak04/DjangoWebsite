from django.urls import path
from . import views 


urlpatterns = [
    path('sign-up/', views.register_pg, name="register_pg"),
    path('login/', views.login_pg, name="login_pg"),
]

from django.urls import path
from . import views

urlpatterns = [
    path('register/<keyword>/', views.register),
    path('login/<keyword>/', views.login)
]

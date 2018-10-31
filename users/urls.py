# users/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('signupo/', views.SignUp.as_view(), name='signup'),
]
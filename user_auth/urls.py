from django.contrib import admin
from django.urls import include, path

from . import views


urlpatterns = [
    path('login/', views.login_user, name='login_user'),
    path('register/', views.register_user, name='register_user'),
]
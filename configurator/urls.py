from django.contrib import admin
from django.urls import include, path
from . import views

urlpatterns = [
    path('/config/new/', views.newConfig),
    path('/config/modify/<int:id>', views.modifyConfig),
    path('/config/delete/<int:id>', views.modifyConfig)
]
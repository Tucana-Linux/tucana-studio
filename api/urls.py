from django.urls import path
from . import views 

urlpatterns = [
    path('configs/', views.getPublicConfigs),
    path('configs/add/', views.addConfig),
    path('configs/<int:id>/', views.getConfigByID),
    path('configs/<int:id>/modify', views.modifyConfig),
    path('configs/<int:id>/delete', views.deleteConfig),
    path('configs/<int:id>/download', views.downloadConfig),
    path('configs/users/<int:userID>', views.getConfigByUser),
]
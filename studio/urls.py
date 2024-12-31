from django.contrib import admin
from django.urls import include, path


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include("api.urls")),
    path('', include("landing.urls")),
    path('configurator/', include("configurator.urls")),
    path('auth/', include('user_auth.urls')),
    path('auth/', include('django.contrib.auth.urls'))
]

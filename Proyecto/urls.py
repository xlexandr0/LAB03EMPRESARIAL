# control_vehicular/urls.py
from django.contrib import admin
from django.urls import path, include
from gestion.views import home

urlpatterns = [
    path('', home, name='home'),
    path('admin/', admin.site.urls),
    path('gestion/', include('gestion.urls')),
]

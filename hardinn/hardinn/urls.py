"""
URL configuration for hardinn project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from .import views
from django.contrib import admin
from django.contrib import admin
from django.urls import path, include

from authentication.views import index
from django.views.generic.base import RedirectView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('admin/', RedirectView.as_view(url='/admin'),name="admin"),
    path("", include("authentication.urls")),
    path('hardinn/template/pc.html', views.pc),
    path('hardinn/template/phone.html', views.phone),
    path('', views.index),
    
]


# urlpatterns = [
#     path('admin/', admin.site.urls),
#     path('', views.index),
#     path('hardinn/template/pc.html', views.pc),
#     path('hardinn/template/phone.html', views.phone),

# ]
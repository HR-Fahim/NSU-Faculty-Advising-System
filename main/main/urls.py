"""
URL configuration for main project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.views.generic import TemplateView
from django.urls import path, re_path
from app import views
#from login.views import manifest_json, logo_png

urlpatterns = [
    path('admin/', admin.site.urls),
    #path('', views.index, name='index'),
    #path('', views.index, name='base'),
    #path('login/', TemplateView.as_view(template_name='login.html')),
    #path('manifest.json', manifest_json, name='manifest-json'),
    #path('logo192.png', logo_png, name='logo-png'),
    #path('Login/', TemplateView.as_view(template_name='index.html')),
    re_path(r'^.*$', TemplateView.as_view(template_name='index.html')),

]

"""projeto URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
import imp

from django.contrib import admin
from django.http import HttpResponse
from django.urls import path


def my_home(request):
    return HttpResponse ("<h1>Hello my baby</h1>")

def sobre(request):
    return HttpResponse("<h1>Assim somos nós</h1>")

def contatos(request):
    return HttpResponse("<h1>Ligue pra mim</h1>")


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', my_home),
    path('sobre/', sobre),
    path('contatos', contatos)

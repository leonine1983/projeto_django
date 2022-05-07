from django.urls import path

from recipes.views import my_home

urlpatterns = [
    path('', my_home),

]



from django.urls import path
from . import views


urlpatterns = [
    path('', views.show_form, name='show_form'),
    path('form1', views.show_form, name='show_form')
]
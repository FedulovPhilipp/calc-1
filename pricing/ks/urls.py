from django.urls import path
from . import views


urlpatterns = [
    path('', views.show_ks, name='show_ks'),
    path('ks', views.show_ks, name='show_ks')
]
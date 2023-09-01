from django.urls import path
from . import urls

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'), ]
from django.urls import path
from .views import *

urlpatterns = [
    path('', ThemeHome.as_view(), name='home'),
    path('theme/<int:pk>', ShowTheme.as_view(), name='theme'),
    path('generate_pdf', generate_pdf, name='generate_pdf'),
]

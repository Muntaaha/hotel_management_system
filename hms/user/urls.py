from django.urls import path
from .views import *

urlpatterns = [
    path('',home, name="home"),
    path('guest_register/', guest_register, name="guest_register"),

]
from django.urls import path
from .views import *


app_name = 'account'
urlpatterns = [
    path('login', log_in, name='login'),
    path('logout', log_out, name='logout'),
    path('register', sign_up, name='register'),
]
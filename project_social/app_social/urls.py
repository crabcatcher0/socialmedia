from django.urls import path
from .views import *


urlpatterns = [
    path('', home, name='home'),
    path('signup', register, name='signup'),
]

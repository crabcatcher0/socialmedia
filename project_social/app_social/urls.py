from django.urls import path
from .views import *


urlpatterns = [
    path('', home, name='home'),
    path('login/', login_view, name='login'),
    path('signup', register, name='signup'),
    path('profile', profile, name='profile'),
]

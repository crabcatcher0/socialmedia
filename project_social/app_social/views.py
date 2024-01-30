from django.shortcuts import render, redirect
from django.shortcuts import get_object_or_404
from django.contrib import messages
from django.contrib.auth import authenticate, login
from .forms import RegisterForm

def home(request):
    return render(request, 'index.html')


def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            messages.success(request, 'Successfully Loggedin.')
            return redirect('profile')
    return render(request, 'login.html')


def register(request):
    register_form_data = RegisterForm()

    if request.method == 'POST':
        register_form_data = RegisterForm(request.POST)

        if register_form_data.is_valid():
            register_form_data.save()
            messages.success(request, 'Successfully created account. Please Login')
            return redirect('login')
        
    context = {
        'register_form_data': register_form_data
    }

    return render (request, 'signup.html', context)



def profile(request):
    return render(request, 'profile.html')
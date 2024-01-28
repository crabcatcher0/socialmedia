from django.shortcuts import render, redirect
from django.shortcuts import get_object_or_404
from django.contrib import messages
from .forms import UserForm



def home(request):

    return render(request, 'index.html')



def register(request):
    register_form_data = UserForm()
    
    if request.method == 'POST':
        register_form_data = UserForm(request.POST)

        if register_form_data.is_valid():
            register_form_data.save()
            messages.success (request, 'Successfully created account.')
            return redirect('home')

    context = {
        'register_form_data': register_form_data,
    }

    return render(request, 'signup.html', context)


def profile(request):
    return render(request, 'profile.html')
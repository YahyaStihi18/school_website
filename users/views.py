from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import *



@login_required()
def profile(request):
    return render(request,'users/profile.html')

    
def register(request):
    if request.method == 'POST':
        form = UserRegisterFrom(request.POST)
        if form.is_valid():
            username=form.cleaned_data['username']
            form.save()
            messages.success(request,f'{username} registred seccessfuly, Log in with your username/password now.')
            return redirect ('login')
    else:
        form = UserRegisterFrom()
    return render(request, 'users/register.html', {'form': form})

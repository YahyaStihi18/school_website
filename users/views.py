from django.shortcuts import render,redirect,HttpResponse
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import *
from .models import *



@login_required()
def profile(request):

    user = request.user

    if Profile.objects.filter(user=user).exists():    
        profile = Profile.objects.get(user=user)
        form = ProfileForm(instance=profile)
        if request.method == 'POST':
            form = ProfileForm(request.POST,request.FILES,instance=profile)
            if form.is_valid():
                form.save()
                messages.success(request, 'Profile info updated successfuly')
                return redirect('profile')
    else:
        form = ProfileForm
        
        if request.method == 'POST':
            form = ProfileForm(request.POST,request.FILES)
            if form.is_valid():
                instance = form.save(commit=False)
                instance.user = request.user
                instance.save()
                messages.success(request, 'Profile info updated successfuly')
                return redirect('profile')


    context = {
        'form':form,
        }
    return render(request,'users/profile.html',context)

    
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

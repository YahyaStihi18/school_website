from django.shortcuts import render,redirect,HttpResponse,HttpResponseRedirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.exceptions import PermissionDenied
from .forms import *
from .models import *
from core.models import Course



@login_required()
def profile(request):

    user = request.user
    announcements = Announcement.objects.filter(user=user).order_by('date').reverse()
    courses = Course.objects.filter(user=user).order_by('date').reverse()
    if Profile.objects.filter(user=user).exists():    
        profile = Profile.objects.get(user=user)
        form = ProfileForm(instance=profile)
        if request.method == 'POST' and 'ProfileForm' in request.POST:
            form = ProfileForm(request.POST,request.FILES,instance=profile)
            if form.is_valid():
                form.save()
                messages.success(request, 'Profile info updated successfully.')
                return redirect('profile')
    else:
        form = ProfileForm
        
        if request.method == 'POST' and 'ProfileForm' in request.POST:
            form = ProfileForm(request.POST,request.FILES)
            if form.is_valid():
                instance = form.save(commit=False)
                instance.user = request.user
                instance.save()
                messages.success(request, 'Profile info updated successfully.')
                return redirect('profile')

    if request.method == 'POST' and 'AnnouncementForm' in request.POST:
            form2 = AnnouncementForm(request.POST)
            if form2.is_valid():
                instance = form2.save(commit=False)
                instance.user = request.user
                instance.save()
                messages.success(request, 'Announcemen added successfully')
                return redirect('profile')
    form2 = AnnouncementForm
    context = {
        'form':form,
        'form2':form2,
        'courses':courses,
        'announcements':announcements,
        }
    return render(request,'users/profile.html',context)

@login_required
def delete_announcement(request, pk):
    user = request.user
    announcement = Announcement.objects.get(pk=pk)
    if announcement.user == user :
        announcement.delete()
        messages.warning(request, 'Announcement deleted successfully!.') 
        return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))
    else:
        raise PermissionDenied()


    
def register(request):
    if request.method == 'POST':
        form = UserRegisterFrom(request.POST)
        if form.is_valid():
            username=form.cleaned_data['username']
            form.save()
            messages.success(request,f'{username} registred seccessfully, Log in with your username/password now.')
            return redirect ('login')
    else:
        form = UserRegisterFrom()
    return render(request, 'users/register.html', {'form': form})

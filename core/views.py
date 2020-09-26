from django.shortcuts import render,HttpResponseRedirect,redirect
from django.contrib.auth.decorators import login_required
from django.core.exceptions import PermissionDenied
from django.contrib import messages
from .forms import CourseForm,LessonForm
from .models import *
from users.models import Announcement

def index(request):
    return render(request,'core/index.html')

def classroom(request):
    courses = Course.objects.all()
    announcements = Announcement.objects.all().order_by('date').reverse()
    context = {
        'courses':courses,
        'announcements':announcements,
    }
    return render(request,'core/classroom.html',context)



@login_required
def add_course(request):
    user = request.user
    form = CourseForm
    context = {
        'form':form,
    }
    if request.method == 'POST':
            form = CourseForm(request.POST,request.FILES)
            if form.is_valid():
                instance = form.save(commit=False)
                instance.user = request.user
                instance.save()
                
    return render (request,'core/add_course.html',context)


@login_required
def add_lesson(request):
    user = request.user
    form = LessonForm
    context = {
        'form':form,
    }
    if request.method == 'POST':
            form = LessonForm(request.POST,request.FILES)
            if form.is_valid():
                instance = form.save(commit=False)
                instance.user = request.user
                instance.save()
                messages.success(request,"Lesson added successfully")
                return redirect('profile')
                
    return render (request,'core/add_lesson.html',context)


@login_required
def delete_course(request,pk):
    user = request.user
    course = Course.objects.get(pk=pk)
    if course.user == user :
        course.delete() 
        messages.warning(request, 'Course deleted successfully!.')
        return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))
    else:
        raise PermissionDenied()


@login_required
def delete_lesson(request,pk):
    user = request.user
    lesson = Lesson.objects.get(pk=pk)
    if lesson.user == user :
        lesson.delete() 
        messages.warning(request, 'Lesson deleted successfully!.')
        return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))
    else:
        raise PermissionDenied()
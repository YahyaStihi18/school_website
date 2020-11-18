from django.shortcuts import render,HttpResponseRedirect,redirect
from django.contrib.auth.decorators import login_required
from django.core.exceptions import PermissionDenied
from django.contrib import messages
from .forms import CourseForm,LessonForm
from .models import *
from users.models import Profile
from users.models import Announcement
from django.contrib.auth.models import User
from django.db.models import Count
from django.db.models import Q
from django.views.generic import ListView

def index(request):
    return render(request,'core/index.html')

def classroom(request):
    staff = User.objects.filter(is_staff=True).annotate(total_course=Count('course',distinct=True)).annotate(total_lesson=Count('lesson',distinct=True))
    teachers = staff.filter(is_superuser=False)
    courses = Course.objects.all().order_by('date').reverse()
    lessons = Lesson.objects.all().order_by('date').reverse()
    announcements = Announcement.objects.all().order_by('date').reverse()


    context = {
        'teachers':teachers,
        'courses':courses,
        'lessons':lessons,
        'announcements':announcements,
    }
    return render(request,'core/classroom.html',context)


def view_profile(request,pk):
    profile = Profile.objects.get(pk=pk)
    user = profile.user

    totals = User.objects.filter(username=user).annotate(total_course=Count('course',distinct=True)).annotate(total_lesson=Count('lesson',distinct=True))
    announcements = Announcement.objects.filter(user=user).order_by('date').reverse()
    courses = Course.objects.filter(user=user).order_by('date').reverse()
    lessons = Lesson.objects.filter(user=user).order_by('date').reverse()

    context={
        'user':user,
        'courses':courses,
        'lessons':lessons,
        'announcements':announcements,
        'totals':totals,
        'profile':profile,} 
    return render (request,'core/view_profile.html',context)


def view_course(request,pk):
    course = Course.objects.get(pk=pk)
    context={
        'course':course,
    }
    return render (request,'core/view_course.html',context)

def view_lesson(request,pk):
    lesson = Lesson.objects.get(pk=pk)
    context={
        'lesson':lesson,
    }
    return render (request,'core/view_lesson.html',context)


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
            return redirect('profile')
    return render (request,'core/add_course.html',context)

@login_required
def edit_course(request,pk):
    user = request.user
    course = Course.objects.get(pk=pk)

    if course.user == user:
        pass
    else:
        raise PermissionDenied

    form = CourseForm(instance=course)
    context={'form':form}
    if request.method == 'POST':
            form = CourseForm(request.POST,request.FILES,instance=course)
            if form.is_valid():
                form.save()
                messages.success(request, 'Course info updated successfully.')
                return redirect('profile')
    return render(request,'core/add_course.html',context)

@login_required
def delete_course(request,pk):
    user = request.user
    course = Course.objects.get(pk=pk)
    if course.user == user:
        pass
    else:
        raise PermissionDenied

    if course.user == user :
        course.delete() 
        messages.warning(request, 'Course deleted successfully!.')
        return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))
    else:
        raise PermissionDenied()



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
def edit_lesson(request,pk):
    user = request.user
    lesson = Lesson.objects.get(pk=pk)

    if lesson.user == user:
        pass
    else:
        raise PermissionDenied

    form = LessonForm(instance=lesson)
    context={'form':form}
    if request.method == 'POST':
            form = LessonForm(request.POST,request.FILES,instance=lesson)
            if form.is_valid():
                form.save()
                messages.success(request, 'Lesson info updated successfully.')
                return redirect('profile')
    return render(request,'core/add_lesson.html',context)

@login_required
def delete_lesson(request,pk):
    user = request.user
    lesson = Lesson.objects.get(pk=pk)
    
    if lesson.user == user:
        pass
    else:
        raise PermissionDenied

    if lesson.user == user :
        lesson.delete() 
        messages.warning(request, 'Lesson deleted successfully!.')
        return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))
    else:
        raise PermissionDenied()


def searchview(request):
    word = request.GET.get('q')  

    lesson_result = Lesson.objects.filter(Q(title__icontains=word))
    lesson_result_count = lesson_result.count()
    course_result = Course.objects.filter(Q(title__icontains=word))
    course_result_count = course_result.count()
    search_reasult_count = lesson_result_count + course_result_count


    context = {
            'lesson_result':lesson_result,
            'course_result':course_result,
            'lesson_result_count':lesson_result_count,
            'course_result_count':course_result_count,
            'search_reasult_count':search_reasult_count,
            }
    return render(request,'core/search_view.html',context)
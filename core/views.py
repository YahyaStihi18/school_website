from django.shortcuts import render,HttpResponseRedirect,redirect
from django.contrib.auth.decorators import login_required
from django.core.exceptions import PermissionDenied
from django.contrib import messages
from .forms import CourseForm

from .models import *

def index(request):
    return render(request,'core/index.html')



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
                messages.success(request, 'Course saved successfully.')
                return redirect('profile')
                
    return render (request,'core/add_course.html',context)



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



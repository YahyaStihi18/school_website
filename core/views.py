from django.shortcuts import render,HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.core.exceptions import PermissionDenied
from django.contrib import messages

from .models import *

def index(request):
    return render(request,'core/index.html')



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



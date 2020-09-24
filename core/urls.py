from django.urls import path
from .views import *

urlpatterns = [
    path('',index,name='index'),
    path('profile/delete_course/<int:pk>/',delete_course,name='delete_course'),
    path('profile/add_course/',add_course,name='add_course')

]

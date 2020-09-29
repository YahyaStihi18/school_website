from django.urls import path
from .views import *

urlpatterns = [
    path('',index,name='index'),
    path('classroom/',classroom,name='classroom'),
    path('classroom/view_course/<int:pk>',view_course,name='view_course'),
    path('classroom/view_lesson/<int:pk>',view_lesson,name='view_lesson'),


    path('profile/add_course/',add_course,name='add_course'),
    path('profile/edit_course/<int:pk>/',edit_course,name='edit_course'),
    path('profile/delete_course/<int:pk>/',delete_course,name='delete_course'),

    path('profile/add_lesson/',add_lesson,name='add_lesson'),
    path('profile/edit_lesson/<int:pk>/',edit_lesson,name='edit_lesson'),
    path('profile/delete_lesson/<int:pk>/',delete_lesson,name='delete_lesson'),


]

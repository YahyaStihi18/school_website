from django.urls import path
from .views import *

urlpatterns = [
    path('',index,name='index'),

    
    path('profile/add_course/',add_course,name='add_course'),
    path('profile/delete_course/<int:pk>/',delete_course,name='delete_course'),
    path('profile/add_lesson/',add_lesson,name='add_lesson'),
    path('profile/delete_lesson/<int:pk>/',delete_lesson,name='delete_lesson'),


]

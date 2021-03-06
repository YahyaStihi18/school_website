from django import forms
from django.contrib.auth.models import User
from .models import Course,Lesson


class CourseForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = '__all__'
        exclude = ['user']
    def __init__(self, *args, **kwargs):
        super(CourseForm, self).__init__(*args, **kwargs)
        self.fields['title'].widget.attrs['class'] = 'form-control'
        self.fields['description'].widget.attrs['class'] = 'form-control'

class LessonForm(forms.ModelForm):
    class Meta:
        model = Lesson
        fields = '__all__'
        exclude = ['user']
    def __init__(self, *args, **kwargs):
        super(LessonForm, self).__init__(*args, **kwargs)
        self.fields['title'].widget.attrs['class'] = 'form-control'
        self.fields['description'].widget.attrs['class'] = 'form-control'
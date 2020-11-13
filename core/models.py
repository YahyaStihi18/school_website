from django.db import models
from django.contrib.auth.models import User
from .validators import validate_file_extension,validate_document_extension


class Course(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE,null=True, blank=True)
    title = models.CharField(max_length=70)
    description = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    thumbnail = models.ImageField(default='static/img/teaching.jpg',blank=True,null=True)
    video =  models.FileField()
    
    def __str__(self):
        return self.title



class Lesson(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE,null=True, blank=True)
    title = models.CharField(max_length=70)
    description = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    document = models.FileField(upload_to='video',validators=[validate_document_extension])
    def __str__(self):
        return self.title

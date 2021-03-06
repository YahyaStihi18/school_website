from django.db import models
from django.contrib.auth.models import User
from .validators import validate_file_extension,validate_document_extension
from ckeditor.fields import RichTextField



class Course(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE,null=True, blank=True)
    title = models.CharField(max_length=70)
    description = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    thumbnail = models.ImageField(default='teaching.jpg',blank=True,null=True)
    video =  models.FileField()
    
    def __str__(self):
        return self.title



class Lesson(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE,null=True, blank=True)
    title = models.CharField(max_length=70)
    description = models.CharField(max_length=700)
    date = models.DateTimeField(auto_now_add=True)
    document = models.FileField(upload_to='doc',validators=[validate_document_extension],null=True,blank=True)
    body = RichTextField(default="(No rich text on this lesson!)",null=True,blank=True)
    def __str__(self):
        return self.title

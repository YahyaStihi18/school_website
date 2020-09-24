from django.db import models
from django.contrib.auth.models import User
from .validators import validate_file_extension

class Course(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE,null=True, blank=True)
    title = models.CharField(max_length=200)
    description = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    thumbnail = models.ImageField(default='teaching.jpg',blank=True,null=True)
    video = models.FileField(upload_to='video',validators=[validate_file_extension])
    def __str__(self):
        return self.title

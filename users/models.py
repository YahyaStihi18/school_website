from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE,null=True, blank=True)
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    specialty = models.CharField(max_length=200)
    phone = models.BigIntegerField()
    address = models.CharField(max_length=200)
    bio = models.TextField()
    image = models.ImageField()
    def __str__(self):
        return self.first_name+' '+self.last_name


class Announcement(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE,null=True, blank=True)
    subject = models.CharField(max_length=70)
    date = models.DateTimeField(auto_now_add=True)
    description = models.TextField()
    def __str__(self):
        return self.user.username


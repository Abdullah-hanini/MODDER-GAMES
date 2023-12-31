from django.db import models
from django.contrib.auth.models import User
from Accounts.models import new_user
from groups.models import group
class user_data (models.Model):
    user = models.OneToOneField(new_user, on_delete=models.CASCADE)
    groups = models.ManyToManyField(group, related_name='groups', blank=True)
    profile_picture = models.ImageField(upload_to='profile_pictures', blank=True)
    bio = models.TextField(max_length=500, blank=True)
    
    def __str__(self):
        return self.user

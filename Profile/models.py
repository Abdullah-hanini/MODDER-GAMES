from django.db import models
from django.contrib.auth.models import User


class user (models.Model):
    user = models.OneToOneField(User)
    profile_picture = models.ImageField(upload_to='profile_pictures', blank=True)
    

    def __unicode__(self):
        return self.user.username
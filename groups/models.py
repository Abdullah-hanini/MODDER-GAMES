from django.db import models
from Accounts.models import new_user
# Create your models here.
class group (models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=50)
    members = models.ManyToManyField(new_user, related_name='members', blank=True)
    pending_members = models.ManyToManyField(new_user, related_name='pending_members', blank=True)
    admin = models.ForeignKey(new_user, related_name='admin', on_delete=models.CASCADE)
    def __str__(self):
        return self.name
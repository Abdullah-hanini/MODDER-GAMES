from django.db import models
from django.utils import timezone
from django.contrib.auth.models import AbstractBaseUser ,PermissionsMixin, BaseUserManager   
from django.utils.translation import gettext_lazy
class CustomAccountManager(BaseUserManager):
    def create_user(self, email, user_name, first_name, last_name, phone_number, password, **other_fields):
        if not email:
            raise ValueError(gettext_lazy('You must put an email address'))
        
        email = self.normalize_email(email)
        user = self.model(email=email, user_name=user_name, first_name=first_name, last_name=last_name, phone_number=phone_number, **other_fields)
        user.set_password(password)
        user.save()
        return user


    def create_superuser(self, email, user_name, first_name, password, last_name, phone_number, **other_fields):

        other_fields.setdefault('is_staff', True)
        other_fields.setdefault('is_superuser', True)
        other_fields.setdefault('is_active', True)

        if other_fields.get('is_staff') is not True:
            raise ValueError(
                'Superuser must be assigned to is_staff=True.')
        if other_fields.get('is_superuser') is not True:
            raise ValueError(
                'Superuser must be assigned to is_superuser=True.')

        return self.create_user(email, user_name, first_name,last_name, phone_number, password, **other_fields)
class new_user (AbstractBaseUser, PermissionsMixin):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    user_name = models.CharField(max_length=50 , unique=True)
    email = models.EmailField(gettext_lazy('Email address '),max_length=50 , unique=True)
    phone_number = models.CharField(max_length=50)
    start_date = models.DateTimeField(default=timezone.now)
    birth_date = models.DateField(null=True, blank=True)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_confirmed = models.BooleanField(default=False)
    
    objects = CustomAccountManager()
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ["user_name", "first_name", "last_name", "phone_number"]

    def __str__(self):
        return self.user_name


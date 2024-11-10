from django.db import models
from django.utils import timezone
from django.contrib.auth.models import (
    AbstractBaseUser, BaseUserManager, PermissionsMixin
)

class UserManager(BaseUserManager):
    """Manager for the user"""

    def create_user(self, email, password=None, **extra_fields):
        """Create, save and return user"""
        email = self.normalize_email(email)

        if not email:
            raise ValueError("Please provide email address")
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db) #for saving into multiple dbs

        return user

    def create_superuser(self, email, password=None, **extra_fields):
        """Create and return super user"""
        user = self.create_user(email, password)
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)

        return user

class User(AbstractBaseUser, PermissionsMixin):
    """user in the system """
    email = models.EmailField(max_length=256, unique=True)
    first_name = models.CharField(max_length=256, null=True, blank=True)
    last_name = models.CharField(max_length=256, null=True, blank=True)
    date_of_birth = models.DateField(null=True, blank=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    phone = models.CharField(max_length=15, blank=True)
    bio = models.TextField(blank=True)
    date_joined = models.DateTimeField(default=timezone.now)


    # connects to usermanager class
    objects = UserManager()
    # to use email as username
    USERNAME_FIELD = 'email'

    def __str__(self):
        return self.name

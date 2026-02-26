from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
from django.utils.translation import gettext_lazy as _


class UserManager(BaseUserManager):
    """
    This is the manager for the user model. It has two methods, create_user and create_superuser. The create_user method is used to create a regular user, while the create_superuser method is used to create a superuser. The create_user method takes an email, password, and any extra fields as arguments. It checks if the email is provided, normalizes the email, creates a user instance, sets the password, saves the user, and returns the user. The create_superuser method sets the is_staff and is_superuser fields to True and then calls the create_user method to create the superuser. 
    """

    def create_user(self, email, password=None, **extra_fields):
        """
        
        Creates and saves a User with the given email and password.
        """
        if not email:
            raise ValueError(_('Email must be provided'))

        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)

        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, email, password=None, **extra_fields):
        """
        Creates and saves a superuser with the given email and password.
        """
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError(_('Superuser must have is_staff=True'))

        if extra_fields.get('is_superuser') is not True:
            raise ValueError(_('Superuser must have is_superuser=True'))

        return self.create_user(email, password, **extra_fields)


class User(AbstractBaseUser, PermissionsMixin):

    email = models.EmailField(unique=True)
    name = models.CharField(max_length=250)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = UserManager()

    def __str__(self):
        return self.email
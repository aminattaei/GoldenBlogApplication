from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
from django.utils.translation import gettext_lazy as _
from django.db.models.signals import post_save
from django.dispatch import receiver


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
    """
    This is the user model. It has an email field, a name field, and three boolean fields: is_active, is_staff, and is_superuser. The email field is unique and is used as the username field for authentication. The name field is a CharField with a maximum length of 250 characters. The is_active field indicates whether the user account is active or not. The is_staff field indicates whether the user has staff privileges or not. The is_superuser field indicates whether the user has superuser privileges or not. The USERNAME_FIELD is set to 'email', which means that the email field will be used as
    the username for authentication. The REQUIRED_FIELDS is an empty list, which means that no additional fields are required when creating a superuser. The objects attribute is set to an instance of the UserManager class, which provides the methods for creating users and superusers.
    """

    email = models.EmailField(unique=True)
    name = models.CharField(max_length=250)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = UserManager()

    def __str__(self):
        return self.email



class Profile(models.Model):
    """
    This is the profile model. It has a one-to-one relationship with the user model, which means that each user can have only one profile. The profile model has a bio field, which is a TextField that can be blank. The __str__ method returns the email of the associated user.
    """
    user = models.ForeignKey(User, verbose_name=_("user"), on_delete=models.CASCADE)
    first_name = models.CharField(max_length=250)
    last_name = models.CharField(max_length=250)
    image = models.ImageField(upload_to='profile_images/', blank=True, null=True)
    description = models.TextField(blank=True)
        

    def __str__(self):
        return self.user.email
    

@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
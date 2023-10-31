from django.contrib.auth.models import BaseUserManager, AbstractBaseUser, PermissionsMixin
from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _

class UserManager(BaseUserManager):
    def create_user(self,name, phone, email, password, user_type,**extra_fields):
        if not email:
            raise ValueError(_("The Email must be set"))
        
        email = self.normalize_email(email)
        user = self.model(email=email,phone=phone)
        user.set_password(password)
        user.name = name
        user.user_type = user_type
        user.save(using=self._db)
        return user

    def create_superuser(self, name, phone, email, password, user_type, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        extra_fields.setdefault("is_active", True)

        if extra_fields.get("is_staff") is not True:
            raise ValueError(_("Superuser must have is_staff=True."))
        if extra_fields.get("is_superuser") is not True:
            raise ValueError(_("Superuser must have is_superuser=True."))
        return self.create_user(name, phone, email, password, user_type)


class User(AbstractBaseUser, PermissionsMixin):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    phone = models.CharField(unique=True,  max_length=15)
    user_type = models.CharField(max_length=100)
    password = models.CharField(max_length=200)

    first_name = models.CharField(max_length=30, null=True, blank=True)
    last_name = models.CharField(max_length=30, null=True, blank=True)
    username=models.CharField(max_length=30, null=True, blank=True)

    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_superuser = models.BooleanField(default=False)
    date_joined = models.DateTimeField(default=timezone.now)

    class Meta:
        permissions = [('can_access_admin_panel', 'Can access admin panel')]

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ['name', 'phone', 'user_type',]

    objects = UserManager()

    def __str__(self):
        return self.email
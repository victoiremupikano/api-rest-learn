from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser

# Create your models here.
class UserManager(BaseUserManager):
    def create_user(self, email, name, password=None):
        user=self.model(
            email=email,
            name=name,
            is_active=True,
            staff=False
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, name, password=None):
        user=self.create_user(
            email=email,
            name=name,
            password=password
        )
        user.is_admin=True
        user.save(using=self._db)
        return user

class User(AbstractBaseUser):
    email=models.EmailField(max_length=255,null=False, blank=False, unique=True)
    name=models.CharField(max_length=255,null=False, blank=False)
    is_admin=models.BooleanField(default=False)
    is_active=models.BooleanField(default=False)
    staff=models.BooleanField(default=False)

    objects=UserManager()

    USERNAME_FIELD='email'
    REQUIRED_FIELDS=['name']

    def __str__(self):
        return self.email
    
    def has_perm(self, perm, obj=None):
        return self.is_admin
    
    def has_module_perms(self, app_label):
        "L'utilisateur a-t-il le droit de voir l'application app_label ?"
        return True
    
    @property
    def is_staff(self):
        "L'utilisateur est-il membre du personnel ?"
        return self.is_admin
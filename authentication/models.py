from django.db import models
from django.contrib.auth.models import BaseUserManager,AbstractBaseUser
# Create your models here.
class UserManager(BaseUserManager):
    def create_user(self,email,is_active,name,staff,password=None):
        User=self.model(
            email=email,
            name=name,
            is_active=True,
            staff=False
        )
        User.set_password(password)
        User.save(using=self._db)
        return User

    def create_superuser(self,email,name,password=None):
        User=self.model(
            email=email,
            name=name,
            password=password
        )
        User.is_admin=True
        User.save(using=self._db)
        return User
    
class User(AbstractBaseUser):
    email=models.EmailField(max_length=255,null=False,unique=True)
    name=models.CharField(max_length=255, null=False,blank=False)
    is_active=models.BooleanField(default=True)
    is_admin=models.BooleanField(default=True)
    staff=models.BooleanField(default=False)
    
    objects=UserManager()
    
    USERNAME_FIELD='email'
    REQUIRED_FIELDS=['name']
    
    def __str__(self):
        return self.email
    
    def has_perm(self,perm,obj=None):
        return self.is_admin
    
    def has_module_perms(self,app_label):
        return True


    @property
    def is_admin(self):
        
        return self.is_admin
    
    @is_admin.setter
    def is_admin(self, value):
        if isinstance(value, bool):  # You can add any validation here if needed
            self._is_admin = value
        else:
            raise ValueError("is_admin must be a boolean")
    
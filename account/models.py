from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager
from django.db import models

# Create your models here.
class MyAccountManager(BaseUserManager):

    def create_user(self, first_name,last_name,address,email,mobile_number,profile_pic,date_of_birth,password=None):
        if not email:
            raise ValueError("users must have an email address. ")
        if not mobile_number:
            raise ValueError("users must have a mobile number. ")
        
        user = self.model(
            email = self.normalize_email(email),
            first_name = first_name,
            last_name = last_name,
            address = address,
            mobile_number = mobile_number,
            profile_pic = profile_pic,
            date_of_birth = date_of_birth
        )
        user.set_password(password)
        user.save(using = self.db)
        return user

    def create_superuser(self, first_name,last_name,address,email,mobile_number,profile_pic,date_of_birth,password=None):
        user = self.model(
            email = self.normalize_email(email),
            first_name = first_name,
            last_name = last_name,
            address = address,
            mobile_number = mobile_number,
            profile_pic = profile_pic,
            date_of_birth = date_of_birth
        )
        user.set_password(password)
        user.is_admin = True
        user.is_superuser = True
        user.is_staff = True
        user.save(using = self.db)
        return user



class MyUser(AbstractBaseUser):

    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    date_of_birth = models.DateField()
    address = models.CharField(max_length=250)
    email = models.EmailField(unique=True)
    mobile_number = models.CharField(max_length=20)
    profile_pic = models.FileField(max_length=1000)
    last_login = models.DateField(auto_now=True)
    is_active = models.BooleanField(default=True)
    is_superuser = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=True)


    USERNAME_FIELD = 'email'
    REQUIERD_FIELDS = ['first_name', 'last_name', 'date_of_birth', 'address', 'mobile_number', 'profile_pic']


    objects = MyAccountManager()

    def __str__(self) :
        return self.email



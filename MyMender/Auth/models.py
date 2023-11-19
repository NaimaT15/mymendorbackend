from django.db import models
from django.contrib.auth.models import (
    AbstractBaseUser, BaseUserManager
)

class UserManager(BaseUserManager):
    def create_user(self, identification_number, first_name,last_name, email, password=None):
        
        if not identification_number:
            raise ValueError('Users must have an identification_number')

        user = self.model(
            email=self.normalize_email(email),
            identification_number=identification_number,
            first_name=first_name,
            last_name=last_name,
        )

        user.set_password(password)
        user.save()
        return user
    def create_superuser(self, identification_number, first_name,last_name, email, password):
        user=self.create_user(
            email=self.normalize_email(email),
            identification_number=identification_number,
            first_name=first_name,
            last_name=last_name,
            password=password
        )
        user.is_admin=True
        user.is_staff=True
        user.is_superuser=True
        user.save()
        return user

# class Groupp(models.Model):
#     ID = models.AutoField(primary_key=True)
#     name = models.CharField(max_length=500, null=True)
    
    

class User(AbstractBaseUser):
    id = models.AutoField(primary_key=True)
    email = models.EmailField(
        verbose_name='email address',
        max_length=255,
    )
    identification_number=models.CharField(max_length=255,unique=True,)
    first_name = models.CharField(max_length=500, blank=False, null=False)
    last_name = models.CharField(max_length=500, blank=False, null=False)
    password= models.CharField(max_length=500, blank=False, null=False)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_customer = models.BooleanField(default=False)
    # groups = models.ForeignKey("Groupp",to_field='ID', on_delete=models.CASCADE)
    # groups = models.ForeignKey("Group",to_field='ID', on_delete=models.CASCADE)
    date_created=models.DateTimeField(auto_now_add=True, null=True)
    objects = UserManager()

    USERNAME_FIELD = 'identification_number'
    REQUIRED_FIELDS = ['first_name', 'last_name', 'email']

    def __str__(self):
        return str(self.identification_number)
    def has_perm(self, perm, object=None):
        return self.is_admin
    def has_module_perms(self, app_labe):
        return True

class admin(models.Model):
    ID= models.AutoField(primary_key=True)
    #user_ID = models.ForeignKey(User, to_field='identification_number',on_delete=models.CASCADE)
    user_ID = models.ForeignKey("User",to_field='identification_number', on_delete=models.CASCADE)
    date_created=models.DateTimeField(auto_now_add=True, null=True)
    def __str__(self):
        return str(self.user_ID)

    
class department(models.Model):
    ID= models.AutoField(primary_key=True)
    dep_name=models.CharField(max_length=500, null=True)
    date_created=models.DateTimeField(auto_now_add=True, null=True)
    def __str__(self):
        return str(self.dep_name)
class customer(models.Model):
    ID= models.AutoField(primary_key=True)
    user_ID = models.ForeignKey("User",to_field='identification_number', on_delete=models.CASCADE)
    date_created=models.DateTimeField(auto_now_add=True, null=True)
    def __str__(self):
        return str(self.user_ID)

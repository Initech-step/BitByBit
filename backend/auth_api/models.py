from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.contrib.auth import get_user_model
from django.conf import settings
from rest_framework.authtoken.models import Token
# Create your models here.


class MyUserManager(BaseUserManager):
    def create_user(self, email, first_name, last_name, school, school_short_form, department, set_year, password=None):
        if not email:
            raise ValueError('Users must have an email address')

        user = self.model(
            email=self.normalize_email(email),
            first_name=first_name,
            last_name=last_name,
            school=school,
            school_short_form=school_short_form,
            department=department,
            set_year=set_year
        )

        user.set_password(password)
        user.save(using=self._db)
        Token.objects.create(user=user)

    def create_superuser(self, email, first_name, last_name, school, school_short_form, department, set_year, password=None):
        if not email:
            raise ValueError('Users must have an email address')

        user = self.model(
            email=self.normalize_email(email),
            first_name=first_name,
            last_name=last_name,
            school=school,
            school_short_form=school_short_form,
            department=department,
            set_year=set_year
        )

        user.is_admin = True
        user.set_password(password)
        user.save(using=self._db)
        return user





class Users(AbstractBaseUser):
    email = models.EmailField(unique=True, max_length=200)
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    school = models.CharField(max_length=200)
    school_short_form = models.CharField(max_length=15)
    department = models.CharField(max_length=200)
    set_year = models.IntegerField()
    currently_managing = models.IntegerField(null=True)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)

    objects = MyUserManager()

    #fields that will be prompted for supper user
    REQUIRED_FIELDS = ['first_name', 'last_name', 'school', 'school_short_form', 'department', 'set_year']
    #unique identifier for users
    USERNAME_FIELD = 'email'

    def has_perm(self, perm, obj=None):
        return True
    
    def has_module_perms(self, app_label):
        return True
    
    @property
    def is_staff(self):
        return self.is_admin
    
    def __str__(self):
        return self.email






class B3Groups(models.Model):
    group_name = models.CharField(max_length=200)
    group_description = models.CharField(max_length=250)
    group_department = models.CharField(max_length=100)
    group_school = models.CharField(max_length=200)
    is_open_for_application = models.BooleanField(default=False)

    message_for_new_subscriber = models.TextField(default='I and the admins welcome you.')
    message_for_accepted_applicant = models.TextField(default='You are accepted to be an admin')

    group_creator = models.ForeignKey(get_user_model(), related_name='groups_created', on_delete=models.CASCADE)
    group_admins = models.ManyToManyField(get_user_model(), related_name='group_sub_admins')

    def __str__(self):
        return f'{self.group_name}'





class B3Subcribers(models.Model):
    email = models.EmailField(max_length=200)
    b3_group = models.ForeignKey(B3Groups, related_name='subscribers', on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.email}'




class Posts(models.Model):
    letter_title = models.CharField(max_length=300)
    body = models.TextField()
    b3_group = models.ForeignKey(B3Groups, null=True, related_name='posts', on_delete=models.SET_NULL)
    approved = models.BooleanField(default=True)
    written_by = models.ForeignKey(get_user_model(), related_name='writter', null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return f'{self.letter_title}'




class Applications(models.Model):
    application_message = models.TextField()
    b3_group = models.ForeignKey(B3Groups, on_delete=models.CASCADE)
    applicant = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, related_name='user_applying')

    def __str__(self):
        return f'{self.applicant}'
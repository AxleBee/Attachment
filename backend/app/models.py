from django.db import models
import datetime
from django.contrib.auth.models import (BaseUserManager, AbstractBaseUser)
# Create your models here.


class UserManager(BaseUserManager):

    def create_user(self, username, email, user_type, password=None):
        if username is None:
            raise TypeError('Users must have a username')
        if email is None:
            raise TypeError('Users must have a Email')

        user = self.model(

            username=username,
            user_type=user_type,
            email=self.normalize_email(email)

        )
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, user_type, username, password=None):

        user = self.create_user(

            email,
            user_type=user_type,
            username=username,
            password=password,

        )

        user.is_admin = True
        user.is_superuser = True
        user.is_staff = True
        user.save(using=self._db)
        return user


class User(AbstractBaseUser):

    USER_TYPE_CHOICES = (

        ('employer', "Employer"),
        ('supervisor', "Supervisor"),
        ('student', "Student"),
    )

    email = models.EmailField(max_length=100, unique=True)
    username = models.CharField(max_length=100)
    user_type = models.CharField(max_length=10)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    date_joined = models.DateTimeField(auto_now_add=True)
    last_login = models.DateTimeField(auto_now_add=True)
    updated_profile = models.BooleanField(default=False)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'user_type']

    objects = UserManager()

    def __str__(self):
        return self.email


class Student(models.Model):

    admission_no = models.CharField(max_length=100, unique=True)
    name = models.CharField(max_length=255)
    course = models.CharField(max_length=255)
    year = models.IntegerField(blank=True, null=True)
    photo_url = models.ImageField(upload_to="images/")
    assessed_by_employer = models.BooleanField(default=False)
    user = models.OneToOneField(
        User, primary_key=True, on_delete=models.CASCADE)

    @classmethod
    def get_profile_info(cls, email):
        profile_info = cls.objects.filter(email=email).first()
        return profile_info

    @classmethod
    def update_profile(cls, id, admission_no, name, course):
        cls.objects.filter(pk=id).update(
            admission_no=admission_no, name=name, course=course)
        new_name_object = cls.objects.get(admission_no=admission_no)
        new_name = new_name_object.admission_no
        return new_name


class Attachment(models.Model):
    attachment_name = models.CharField(max_length=100)
    department_name = models.CharField(max_length=100)
    start_date = models.DateField(default=datetime.date.today)
    end_date = models.DateField(default=datetime.date.today)
    student = models.OneToOneField(
        Student, primary_key=True, on_delete=models.CASCADE)

    @classmethod
    def get_profile_info(cls, email):
        attachment_info = cls.objects.get(email=email).first()
        return attachment_info


class LogBook(models.Model):
    date = models.DateField(auto_now=False)
    activity = models.CharField(max_length=1000)
    status = models.BooleanField(default=False)
    student = models.ForeignKey(Student, on_delete=models.CASCADE, )

    def verify(self):
        self.verified = True
        return True


class Supervisor(models.Model):
    name = models.CharField(max_length=255)
    postion = models.CharField(max_length=255)
    phone = models.CharField(max_length=20)
    photo_url = models.ImageField(upload_to="images/")
    user = models.OneToOneField(
        User, primary_key=True, on_delete=models.CASCADE)


class Comments(models.Model):
    comment = models.CharField(max_length=1000)
    supervisor = models.ForeignKey(Supervisor, on_delete=models.CASCADE)
    logbook = models.ForeignKey(LogBook, on_delete=models.CASCADE)

    @classmethod
    def get_comments(cls, id):
        comments = cls.objects.filter(update__id=id)
        return comments

    def save_comment(self):
        self.save()

    def __str__(self):
        return self.comment


class Employer(models.Model):
    name = models.CharField(max_length=255)
    organisation = models.CharField(max_length=255)
    postion = models.CharField(max_length=255)
    phone = models.CharField(max_length=20)
    photo_url = models.ImageField(upload_to="images/")
    user = models.OneToOneField(
        User, primary_key=True, on_delete=models.CASCADE)


class EmployerComment(models.Model):
    comment = models.CharField(max_length=1000)
    student = models.OneToOneField(Student, on_delete=models.CASCADE)

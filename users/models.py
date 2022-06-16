from django.db import models

from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    pass

class Student(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    profile_image = models.ImageField(upload_to='profile_images', max_length=255, blank=True, null=True)
    department = models.CharField(max_length=50)

    def __str__(self):
        return self.user.username


class Collaborator(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    company_name = models.CharField(max_length=100)
    acronym = models.CharField(max_length=20)
    country = models.CharField(max_length=50, null=True, blank=True)
    city = models.CharField(max_length=50,null=True,blank=True)

    def __str__(self):
        return self.user.username



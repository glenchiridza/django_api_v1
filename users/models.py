from django.db import models

from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    pass

class Student(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    profile_image = models.ImageField(upload_to='profile_images', max_length=255, blank=True, null=True)
    department = models.CharField(max_length=100)

    def __str__(self):
        return self.user.username


class Collaborator(models.Model):


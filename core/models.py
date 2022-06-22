from django.db import models
from django.contrib.auth import get_user_model
from django.urls import reverse
from django.utils.safestring import mark_safe
User = get_user_model()


class Post(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class LeaderBoard(models.Model):
    contributor = models.ForeignKey(User, on_delete=models.CASCADE)
    department = models.CharField(max_length=100)
    count = models.IntegerField()

    @property
    def update_leader_board(self):
        url = reverse('')
        a = '''<a href="{}">Update leader board</a>'''
        return mark_safe(a)

    def __str__(self):
        return f'contributions by {self.contributor}'
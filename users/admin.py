from django.contrib import admin

from .models import User,Student,Collaborator

admin.site.register(User)
admin.site.register(Student)
admin.site.register(Collaborator)

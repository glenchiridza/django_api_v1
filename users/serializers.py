from rest_framework import serializers
from rest_auth.registration.serializers import RegisterSerializer
from allauth.account.adapter import get_adapter

from .models import User, Collaborator, Student


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        field = (
            'id', 'email', 'username', 'password'
        )

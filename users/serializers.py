from rest_framework import serializers
from rest_auth.registration.serializers import RegisterSerializer
from allauth.account.adapter import get_adapter

from .models import User, Collaborator, Student


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        field = (
            'id', 'email', 'username', 'password',
        )


# creating custom registration form using rest-auth

class CustomRegisterSerializer(RegisterSerializer):
    class Meta:
        model = User
        fields = (
            'id', 'username', 'email', 'password',
        )

    # these are fields to be presented to user, to fill in
    # and are validated before proceeding

    def get_cleaned_data(self):
        return {
            'username': self.validated_data.get('username', ''),
            'password1': self.validated_data.get('password1', ''),
            'password2': self.validated_data.get('password2', ''),
            'email': self.validated_data.get('email', ''),

        }

    def save(self, request):
        adapter = get_adapter()
        user = adapter.new_user(request)
        self.cleaned_data = self.get_cleaned_data()
        user.save()

        adapter.save_user(request, user, self)

        return user


class CollaboratorProfileUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Collaborator
        fields = ('company_name', 'acronym', 'country', 'city',)


class StudentsProfileUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = (
            'first_name', 'last_name', 'profile_image', 'department',
        )


class StudentsProfileRetrieveSerializer(serializers.ModelSerializer):
    # make readonly so that it cant be applicable for update with the rest of the other fields
    department = serializers.CharField(max_length=5-, read_only=True)

    class Meta:
        model = Student
        fields = (
            'first_name','last_name','profile_image'
        )
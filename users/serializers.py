from django.contrib.auth.password_validation import validate_password
from django.core.validators import validate_email, ValidationError
from rest_framework import serializers

from .models import User


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        writable_fields = ('username', 'password', 'email')
        read_only_fields = ('date_joined', 'id', 'last_login', 'is_staff')
        fields = tuple(set(read_only_fields + writable_fields))

        extra_kwargs = {'password': {'write_only': True}}

    def validate_email(self, data):
        try:
            validate_email(data)
        except ValidationError as e:
            raise ValidationError({'email': e})
        return data

    def create(self, validated_data):
        password = validated_data.pop('password')
        user = User(**validated_data)
        user.set_password(password)
        user.save()
        return user

    def validate_password(self, data):
        try:
            validate_password(data)
        except ValidationError as e:
            raise ValidationError({'password': e})
        return data

from django.contrib.auth.password_validation import validate_password
from django.core.validators import validate_email, ValidationError
from rest_framework import serializers

from .models import User


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User

        exclude = ('is_superuser', 'is_staff', )
        read_only_fields = ('date_joined',)
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

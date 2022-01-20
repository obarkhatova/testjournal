from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.postgres.fields import CICharField, CIEmailField


class User(AbstractUser):
    username = CICharField(max_length=150, unique=True)
    firstname = models.CharField(max_length=150, blank=True)
    lastname = models.CharField(max_length=150, blank=True)
    email = CIEmailField(unique=True)
    is_active=models.BooleanField(default=True)
    date_joined = models.DateTimeField(auto_now_add=True, editable=False)

    EMAIL_FIELD = "email"
    USERNAME_FIELD = "username"
    REQUIRED_FIELDS = ["email"]

    class Meta:
        verbose_name = "user"
        verbose_name_plural = "users"

    def get_ful_name(self):
        return ' '.join(filter(None, [self.firstname, self.lastname]))

    def __str__(self):
        return self.get_full_name() or self.username



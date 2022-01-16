from django.db import models
from users.models import User


class Blog(models.Model):
    title = models.CharField(max_length=200, null=True)
    created = models.DateTimeField(auto_now_add=True)
    author = models.OneToOneField(User,
                                  on_delete=models.CASCADE,
                                  primary_key=True,
                                  related_name='blog')
    subscribers = models.ManyToManyField('settings.AUTH_USER_MODEL',
                                         through='Subscriptions',
                                         related_name='subscriptions')
    class Meta:
        ordering = ['-created']

    def __str__(self):
        return f'{self.title or "Unknown"}:  {self.created}'

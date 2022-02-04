from django.db import models
from django.conf import settings

from blogs.models import Blog


User = settings.AUTH_USER_MODEL


class Subscription(models.Model):
    blog = models.ForeignKey(Blog, null=False, related_name='subscriptions',
                             on_delete=models.CASCADE)
    user = models.ForeignKey(User, null=False, related_name='subscriptions',
                             on_delete=models.CASCADE)

    class Meta:
        unique_together = (("blog", "user"),)


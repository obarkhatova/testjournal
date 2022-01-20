from django.db import models

from blogs.models import Blog
from users.models import User


class Subscription(models.Model):
    blog = models.ForeignKey(Blog, null=False, related_name='subscriptions',
                             on_delete=models.CASCADE)
    user = models.ForeignKey(User, null=False, related_name='subscriptions',
                             on_delete=models.CASCADE)

    class Meta:
        unique_together = (("blog", "user"),)


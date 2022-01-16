# from django.db import models
#
# from blogs.models import Blog
# from users.models import User
#
#
# toppings = models.ManyToManyField('Topping', through='ToppingAmount', related_name='pizzas')
#
# class Subscription(models.Model):
#     blog = models.ForeignKey(Blog, null=False, related_name='subscriptions')
#
#     user = models.ForeignKey(User, null=False, related_name='subscriptions')
#
#     class Meta:
#         unique_together = (("blog", "user"),)

from django.db.models import Subquery
from rest_framework.generics import ListAPIView
from rest_framework.mixins import ListModelMixin

from .models import Subscription
from .serializers import FeedSerializer
from posts.models import Post


class FeedView(ListAPIView):
    serializer_class = FeedSerializer

    def get_queryset(self):
        user = self.request.user
        blogs_subscribed_to = Subscription.objects.filter(user=user).values('blog_id')
        return Post.objects.filter(blog__in=blogs_subscribed_to).order_by('-created')


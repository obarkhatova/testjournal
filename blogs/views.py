from django.contrib.auth.mixins import LoginRequiredMixin
from rest_framework import status
from rest_framework.generics import GenericAPIView
from rest_framework.mixins import CreateModelMixin, DestroyModelMixin
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated


from subscriptions.models import Subscription
from .serializers import SubscribtionEditSerializer


class SubscriptionCreateView(CreateModelMixin,
                             DestroyModelMixin,
                             GenericAPIView):
    serializer_class = SubscribtionEditSerializer
    permission_classes = [IsAuthenticated]

    def post(self, request, *args, **kwargs):
        data = {'blog': kwargs['blog'],
                'user': request.user.id}
        serializer = self.get_serializer(data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def delete(self,  request, *args, **kwargs):
        data = {'blog': kwargs['blog'],
                'user': request.user.id}
        try:
            instance = Subscription.objects.get(blog_id=data['blog'],
                                                user_id=data['user'])
            self.perform_destroy(instance)
        except Subscription.DoesNotExist:
            pass
        return Response(status=status.HTTP_204_NO_CONTENT)



from rest_framework import status
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet


from .models import Post
from .serializers import PostSerializer, PostReadSerialiser


class PostViewSet(ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticated]
    ordering_fields = ['id', 'name', 'criticality', 'active', 'has_redef']
    ordering = ['-published']

    def get_object(self):
        super().get_object()
    @action(
        methods=["post"],
        detail=True,
        serializer_class=PostReadSerialiser,
        url_path='read',
    )
    def post_read(self, request, *args, **kwargs):
        data = {'user': request.user,
                'post': kwargs.get('pk')
        }
        serializer = self.get_serializer(data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)







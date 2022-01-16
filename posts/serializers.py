from rest_framework import serializers

from .models import Post
from .utils import status_from_int_to_str
from blogs.models import Blog


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        writeable_fields = ['title', 'content']
        read_only_fields = ['created', 'updated', 'published', 'status',
                            'blog']
        fields = writeable_fields + read_only_fields

    def create(self, validated_data):
        post = Post(**validated_data)
        user = self.context['request'].user
        blog = Blog.objects.get(author__username=user.username)
        post.blog = blog
        post.save()
        return post

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        status = status_from_int_to_str(representation['status'])
        representation.update({'status': status})
        return representation




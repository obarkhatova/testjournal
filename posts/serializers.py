from rest_framework import serializers
from rest_framework import validators

from .models import Post, PostRead
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


class PostReadSerialiser(serializers.ModelSerializer):
    class Meta:
        model = PostRead
        fields = '__all__'

    def run_validators(self, value):
        for validator in self.validators:
            if isinstance(validator, validators.UniqueTogetherValidator):
                self.validators.remove(validator)
        super().run_validators(value)

    def create(self, validated_data):
        try:
            return PostRead.objects.get(post=validated_data['post'],
                                        user=validated_data['user'])
        except PostRead.DoesNotExist:
            return super().create(validated_data)

    def to_internal_value(self, data):
        try:
            post_obj = Post.objects.get(pk=data['post'])
            data.update({'post': post_obj})
            return data
        except Post.DoesNotExist:
            raise serializers.ValidationError(f'Post {data["post"]} not found')

    def to_representation(self, instance):
        return {
            'id': instance.id,
            'post_id': instance.post_id,
            'user_id': instance.user_id
        }


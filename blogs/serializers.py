from rest_framework import serializers
from rest_framework import validators
from .models import Blog
from subscriptions.models import Subscription


class SubscribtionEditSerializer(serializers.ModelSerializer):
    blog = serializers.IntegerField(required=True)

    class Meta:
        model = Subscription
        fields = '__all__'

    def validate_blog(self, value):
        try:
            return Blog.objects.get(author_id=value)
        except Blog.DoesNotExist:
            raise serializers.ValidationError("Blog not found")

    def validate(self, data):
        if data['blog'].author == data['user']:
            raise serializers.ValidationError('User can not subscribe their own blog')
        return data

    def run_validators(self, value):
        for validator in self.validators:
            if isinstance(validator, validators.UniqueTogetherValidator):
                self.validators.remove(validator)
        super(SubscribtionEditSerializer, self).run_validators(value)

    def create(self, validated_data):
        try:
            return Subscription.objects.get(blog=validated_data['blog'],
                                            user=validated_data['user'])
        except Subscription.DoesNotExist:
            return super(SubscribtionEditSerializer, self).create(validated_data)

    def to_representation(self, instance):
        return {'id': instance.id,
                'blog_id': instance.blog_id,
                'user_id': instance.user_id
                }


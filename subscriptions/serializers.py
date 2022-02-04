from rest_framework import serializers


class FeedSerializer(serializers.Serializer):
    fields = ['pk', 'blog_id', 'title', 'created']

    def to_representation(self, data):
        return {
            'id': data.pk,
            'created': data.created,
            'title': data.title
        }




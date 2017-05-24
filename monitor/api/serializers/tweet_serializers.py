from rest_framework.serializers import ModelSerializer
from monitor.models import Tweet


__all__ = ['TweetSerializer']


class TweetSerializer(ModelSerializer):

    class Meta:
        model = Tweet
        fields = ('id', 'user', 'text', 'created_at')

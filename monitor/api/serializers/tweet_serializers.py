from rest_framework.serializers import ModelSerializer
from rest_framework.serializers import ReadOnlyField
from monitor.models import Tweet


__all__ = ['TweetSerializer']


class TweetSerializer(ModelSerializer):

    username = ReadOnlyField(source='user.username', read_only=True)

    class Meta:
        model = Tweet
        fields = ('id', 'user', 'text', 'created_at', 'username')

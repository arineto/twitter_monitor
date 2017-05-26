from monitor.models import TweetResponse
from rest_framework.serializers import ModelSerializer
from rest_framework.serializers import ReadOnlyField


__all__ = ['TweetResponseSerializer']


class TweetResponseSerializer(ModelSerializer):

    username = ReadOnlyField(source='user.username', read_only=True)

    class Meta:
        model = TweetResponse
        fields = ('id', 'user', 'tweet', 'text', 'created_at', 'username')

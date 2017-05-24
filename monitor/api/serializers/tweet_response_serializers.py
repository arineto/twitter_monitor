from rest_framework.serializers import ModelSerializer
from monitor.models import TweetResponse


__all__ = ['TweetResponseSerializer']


class TweetResponseSerializer(ModelSerializer):

    class Meta:
        model = TweetResponse
        fields = ('user', 'tweet', 'text')

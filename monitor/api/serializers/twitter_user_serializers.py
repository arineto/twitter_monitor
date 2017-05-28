from monitor.models import TwitterUser
from monitor.tasks import retrieve_tweets
from rest_framework.serializers import ModelSerializer


__all__ = ['TwitterUserSerializer', 'UsernameSerializer']


class TwitterUserSerializer(ModelSerializer):

    class Meta:
        model = TwitterUser
        fields = ('id', 'username', 'status', 'created_at')

    def create(self, validated_data):
        instance = super(TwitterUserSerializer, self).create(validated_data)
        user = self.context.get('request').user
        retrieve_tweets.delay(instance.id, user.id)
        return instance


class UsernameSerializer(ModelSerializer):

    class Meta:
        model = TwitterUser
        fields = ('id', 'username')

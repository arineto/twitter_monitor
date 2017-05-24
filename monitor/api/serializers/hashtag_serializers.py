from rest_framework.serializers import ModelSerializer
from monitor.models import Hashtag


__all__ = ['HashtagSerializer']


class HashtagSerializer(ModelSerializer):

    class Meta:
        model = Hashtag
        fields = ('id', 'name')

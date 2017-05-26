from monitor.api.serializers import TweetResponseSerializer
from monitor.models import TweetResponse
from rest_framework.generics import ListAPIView
from rest_framework.permissions import IsAuthenticated


__all__ = ['TweetResponseListView']


class TweetResponseListView(ListAPIView):

    serializer_class = TweetResponseSerializer
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        return TweetResponse.objects.filter(tweet_id=self.kwargs.get('pk'))

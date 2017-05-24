from monitor.api.serializers import TwitterUserSerializer
from monitor.api.serializers import UsernameSerializer
from monitor.models import TwitterUser
from rest_framework.generics import ListCreateAPIView
from rest_framework.permissions import IsAuthenticated


__all__ = ['TwitterUserView', 'UsernameListView']


class TwitterUserView(ListCreateAPIView):

    queryset = TwitterUser.objects.all()
    serializer_class = TwitterUserSerializer
    permission_classes = (IsAuthenticated,)


class UsernameListView(TwitterUserView):

    serializer_class = UsernameSerializer

from monitor.api.serializers import HashtagSerializer
from monitor.models import Hashtag
from rest_framework.generics import ListAPIView
from rest_framework.permissions import IsAuthenticated


__all__ = ['HashtagListView']


class HashtagListView(ListAPIView):

    queryset = Hashtag.objects.all()
    serializer_class = HashtagSerializer
    permission_classes = (IsAuthenticated,)

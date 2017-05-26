from monitor.api.serializers import TweetResponseSerializer
from monitor.api.serializers import TweetSerializer
from monitor.models import Tweet
from rest_framework.generics import ListAPIView
from rest_framework.generics import RetrieveAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView


__all__ = ['TweetListView', 'TweetRetrieveView', 'TweetReplyView']


class TweetListView(ListAPIView):

    queryset = Tweet.objects.all()
    serializer_class = TweetSerializer
    permission_classes = (IsAuthenticated,)


class TweetRetrieveView(RetrieveAPIView):

    queryset = Tweet.objects.all()
    serializer_class = TweetSerializer
    lookup_fields = ('pk',)
    permission_classes = (IsAuthenticated,)


class TweetReplyView(APIView):

    permission_classes = (IsAuthenticated,)

    def post(self, request, *args, **kwargs):
        try:
            tweet = Tweet.objects.get(pk=kwargs.get('pk'))
            data = request.data
            data.update({
                'user': request.user.pk,
                'tweet': tweet.pk
            })

            serializer = TweetResponseSerializer(data=data)
            serializer.is_valid(raise_exception=True)

            tweet.reply(request.user, data.get('text'))

        except Tweet.DoesNotExist:
            return Response(status=404)

        return Response()

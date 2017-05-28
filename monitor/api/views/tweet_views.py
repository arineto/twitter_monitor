from datetime import datetime
from monitor.api.serializers import TweetResponseSerializer
from monitor.api.serializers import TweetSerializer
from monitor.models import Hashtag
from monitor.models import Tweet
from rest_framework.generics import ListAPIView
from rest_framework.generics import RetrieveAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView


__all__ = ['TweetListView', 'TweetRetrieveView', 'TweetReplyView']


class TweetListView(ListAPIView):

    serializer_class = TweetSerializer
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        queryset = Tweet.objects.all()

        user = self.request.query_params.get('username')
        if user:
            queryset = queryset.filter(user_id=int(user))

        term = self.request.query_params.get('term')
        if term:
            queryset = queryset.filter(text__icontains=term)

        hashtags = self.request.query_params.get('hashtags')
        if hashtags:
            hashtags = [int(h) for h in hashtags.split(',')]
            tags = Hashtag.objects.filter(pk__in=hashtags)
            queryset = queryset.filter(hashtags__in=tags)

        start_date = self.request.query_params.get('start_date')
        if start_date:
            start_date = datetime.strptime(start_date, '%Y-%m-%d')
            start_date = start_date.replace(hour=0, minute=0, second=0)
            queryset = queryset.filter(date__gte=start_date)

        end_date = self.request.query_params.get('end_date')
        if end_date:
            end_date = datetime.strptime(end_date, '%Y-%m-%d')
            end_date = end_date.replace(hour=23, minute=59, second=59)
            queryset = queryset.filter(date__lte=end_date)

        return queryset.order_by('-date')


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

from django.conf import settings
from django.test import TestCase
from django.utils import timezone
from model_mommy import mommy
from monitor.api.serializers import TweetSerializer


class TestTweetSerializer(TestCase):

    def setUp(self):
        self.user = mommy.make('monitor.TwitterUser')
        self.date = timezone.now()

    def test_save(self):
        data = {'user': self.user.id, 'text': 'test', 'date': self.date}
        serializer = TweetSerializer(data=data)
        self.assertTrue(serializer.is_valid())

        instance = serializer.save()
        self.assertEqual(instance.user, self.user)
        self.assertEqual(instance.text, 'test')
        self.assertEqual(instance.date, self.date)

    def test_dump(self):
        tweet = mommy.make('monitor.Tweet')
        serializer = TweetSerializer(instance=tweet)
        self.assertEqual(serializer.data.get('user'), tweet.user.id)
        self.assertEqual(serializer.data.get('text'), tweet.text)
        self.assertEqual(
            serializer.data.get('date'),
            tweet.date.strftime(
                settings.REST_FRAMEWORK.get('DATETIME_FORMAT')
            )
        )
        self.assertEqual(
            serializer.data.get('username'), tweet.user.username
        )

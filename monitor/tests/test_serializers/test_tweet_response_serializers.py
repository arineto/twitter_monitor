from django.test import TestCase
from model_mommy import mommy
from monitor.api.serializers import TweetResponseSerializer


class TestTweetResponseSerializer(TestCase):

    def setUp(self):
        self.user = mommy.make('users.User')
        self.tweet = mommy.make('monitor.Tweet')

    def test_save(self):
        data = {'user': self.user.id, 'tweet': self.tweet.id, 'text': 'test'}
        serializer = TweetResponseSerializer(data=data)
        self.assertTrue(serializer.is_valid())

        instance = serializer.save()
        self.assertEqual(instance.user, self.user)
        self.assertEqual(instance.tweet, self.tweet)
        self.assertEqual(instance.text, 'test')

    def test_dump(self):
        response = mommy.make('monitor.TweetResponse')
        serializer = TweetResponseSerializer(instance=response)
        self.assertEqual(serializer.data.get('user'), response.user.id)
        self.assertEqual(serializer.data.get('tweet'), response.tweet.id)
        self.assertEqual(serializer.data.get('text'), response.text)
        self.assertEqual(
            serializer.data.get('username'), response.user.username
        )

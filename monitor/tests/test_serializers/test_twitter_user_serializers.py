from django.test import TestCase
from model_mommy import mommy
from monitor.api.serializers import TwitterUserSerializer, UsernameSerializer
from monitor.tests.utils.api_mock import RequestMock
import mock


class TestTwitterUserSerializer(TestCase):

    def setUp(self):
        self.user = mommy.make('users.User')
        self.context = {
            'request': RequestMock(self.user)
        }

    def test_save(self):
        data = {'username': 'test'}
        serializer = TwitterUserSerializer(data=data)
        self.assertTrue(serializer.is_valid())

        path = (
            'monitor.api.serializers.twitter_user_serializers.'
            'retrieve_tweets.delay'
        )
        with mock.patch(path, mock.Mock()) as delay:
            serializer.context = self.context
            instance = serializer.save()
            delay.assert_called_with(instance.id, self.user.id)
            self.assertEqual(instance.username, data.get('username'))

    def test_dump(self):
        user = mommy.make('monitor.TwitterUser')
        serializer = TwitterUserSerializer(instance=user)
        self.assertEqual(serializer.data.get('username'), user.username)
        self.assertEqual(serializer.data.get('status'), user.status)


class TestUsernameSerializer(TestCase):

    def test_dump(self):
        user = mommy.make('monitor.TwitterUser')
        serializer = UsernameSerializer(instance=user)
        self.assertEqual(serializer.data.get('username'), user.username)

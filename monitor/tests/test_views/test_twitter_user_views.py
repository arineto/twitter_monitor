from django.test import TestCase
from django.urls import reverse
from model_mommy import mommy
from monitor.models import TwitterUser
from monitor.tests.utils.http_client_mixin import HTTPClientMixin
import mock


class TestTwitterUserView(HTTPClientMixin, TestCase):

    def setUp(self):
        super(TestTwitterUserView, self).setUp()
        self.url = reverse('monitor:users')
        self.users = mommy.make('monitor.TwitterUser', _quantity=3)

    def test_get(self):
        response = self.client.get(self.url)
        self.assertEqual(len(response.data), 3)

        for count, user in enumerate(self.users):
            self.assertEqual(response.data[count].get('id'), user.id)

    def test_post(self):
        self.assertEqual(TwitterUser.objects.count(), 3)

        path = (
            'monitor.api.serializers.twitter_user_serializers.'
            'retrieve_tweets.delay'
        )
        with mock.patch(path, mock.Mock()) as retrieve_tweets:
            response = self.client.post(self.url, {'username': 'test'})
            retrieve_tweets.assert_called()
            self.assertEqual(TwitterUser.objects.count(), 4)
            self.assertEqual(response.data.get('username'), 'test')


class TestUsernameListView(HTTPClientMixin, TestCase):

    def setUp(self):
        super(TestUsernameListView, self).setUp()
        self.users = mommy.make('monitor.TwitterUser', _quantity=3)

    def test_get(self):
        url = reverse('monitor:usernames')
        response = self.client.get(url)
        self.assertEqual(len(response.data), 3)

        for count, user in enumerate(self.users):
            self.assertEqual(
                response.data[count].get('username'), user.username
            )

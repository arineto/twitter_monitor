from django.test import TestCase
from model_mommy import mommy
from monitor.tasks import retrieve_tweets
import mock


class TestRetrieveTweets(TestCase):

    def setUp(self):
        self.auth_user = mommy.make('users.User')
        self.twitter_user = mommy.make('monitor.TwitterUser')

    def test_retrieve_tweets(self):
        path = 'monitor.models.TwitterUser.retrieve_tweets'
        with mock.patch(path, mock.Mock()) as retrieve_mock:
            retrieve_tweets(self.twitter_user.id, self.auth_user.id)
            retrieve_mock.assert_called_with(self.auth_user)

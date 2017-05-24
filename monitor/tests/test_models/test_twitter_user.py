from django.test import TestCase
from mock import patch
from model_mommy import mommy
from monitor.enums import TwitterUserStatusEnum
from monitor.tests.utils.api_mock import APIMock, APIMockError


class TestTwitterUser(TestCase):

    def setUp(self):
        self.user = mommy.make('monitor.TwitterUser', username='test')

    def test__str__(self):
        self.assertEqual(str(self.user), 'test')

    def test_update_status(self):
        self.assertEqual(self.user.status, TwitterUserStatusEnum.SEARCHING)

        self.user.update_status(TwitterUserStatusEnum.VALID)
        self.assertEqual(self.user.status, TwitterUserStatusEnum.VALID)

        self.user.update_status(TwitterUserStatusEnum.INVALID)
        self.assertEqual(self.user.status, TwitterUserStatusEnum.INVALID)

    def test_retrieve_tweets(self):
        with patch('monitor.models.api', APIMock()) as api_mock:
            self.user.retrieve_tweets()
            self.assertEqual(self.user.tweet_set.count(), 5)

            for tweet in api_mock.get_user('').timeline(1):
                self.assertTrue(
                    self.user.tweet_set.filter(tweet_id=tweet.id).exists()
                )

            self.assertEqual(self.user.status, TwitterUserStatusEnum.VALID)

    def test_retrieve_tweets_error(self):
        with patch('monitor.models.api', APIMockError()):
            self.user.retrieve_tweets()
            self.assertEqual(self.user.status, TwitterUserStatusEnum.INVALID)

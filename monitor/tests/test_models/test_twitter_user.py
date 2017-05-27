from django.test import TestCase
from mock import patch
from model_mommy import mommy
from monitor.enums import TwitterUserStatusEnum
from monitor.tests.utils.api_mock import APIMock, APIMockError


class TestTwitterUser(TestCase):

    def setUp(self):
        self.user = mommy.make('monitor.TwitterUser', username='test')
        self.auth_user = mommy.make('users.User')
        self.social_user = mommy.make(
            'social_django.UserSocialAuth', user=self.auth_user,
            extra_data={
                'access_token': {
                    'oauth_token': '',
                    'oauth_token_secret': ''
                }
            }
        )

    def test__str__(self):
        self.assertEqual(str(self.user), 'test')

    def test_update_status(self):
        self.assertEqual(self.user.status, TwitterUserStatusEnum.SEARCHING)

        self.user.update_status(TwitterUserStatusEnum.VALID)
        self.assertEqual(self.user.status, TwitterUserStatusEnum.VALID)

        self.user.update_status(TwitterUserStatusEnum.INVALID)
        self.assertEqual(self.user.status, TwitterUserStatusEnum.INVALID)

    def test_retrieve_tweets(self):
        with patch('monitor.models.get_api', APIMock):
            self.user.retrieve_tweets(self.auth_user)
            self.assertEqual(self.user.tweet_set.count(), 5)
            self.assertEqual(self.user.status, TwitterUserStatusEnum.VALID)

    def test_retrieve_tweets_error(self):
        with patch('monitor.models.get_api', APIMockError):
            self.user.retrieve_tweets(self.auth_user)
            self.assertEqual(self.user.status, TwitterUserStatusEnum.INVALID)

from django.test import TestCase
from mock import patch
from model_mommy import mommy
from monitor.tests.utils.api_mock import APIMock


class TestTweet(TestCase):

    def setUp(self):
        self.user = mommy.make('users.User')
        self.tweet = mommy.make('monitor.Tweet', tweet_id='123')
        self.social_user = mommy.make(
            'social_django.UserSocialAuth', user=self.user,
            extra_data={
                'access_token': {
                    'oauth_token': '',
                    'oauth_token_secret': ''
                }
            }
        )

    def test__str__(self):
        self.assertEqual(
            str(self.tweet),
            '{} - {}'.format(
                self.tweet.user, self.tweet.date.strftime('%d/%m/%Y %H:%I')
            )
        )

    def test_reply(self):
        with patch('monitor.models.get_api', APIMock):
            self.assertFalse(self.tweet.tweetresponse_set.exists())
            self.tweet.reply(self.user, 'test reply')
            self.assertTrue(self.tweet.tweetresponse_set.exists())
            self.assertEqual(self.tweet.tweetresponse_set.count(), 1)

            response = self.tweet.tweetresponse_set.get()
            self.assertEqual(response.response_id, '123')
            self.assertEqual(response.user, self.user)
            self.assertEqual(response.tweet, self.tweet)
            self.assertEqual(response.text, 'test reply')

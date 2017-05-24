from django.test import TestCase
from model_mommy import mommy


class TestTweetResponse(TestCase):

    def setUp(self):
        self.response = mommy.make('monitor.TweetResponse')

    def test__str__(self):
        self.assertEqual(
            str(self.response),
            '{} ({})'.format(str(self.response.user), str(self.response.tweet))
        )

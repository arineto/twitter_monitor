from django.test import TestCase
from django.urls import reverse
from model_mommy import mommy
from monitor.tests.utils.http_client_mixin import HTTPClientMixin


class TestTweetResponseListView(HTTPClientMixin, TestCase):

    def setUp(self):
        super(TestTweetResponseListView, self).setUp()
        self.tweet = mommy.make('monitor.Tweet')
        self.response = mommy.make('monitor.TweetResponse', tweet=self.tweet)

    def test_get(self):
        url = reverse('monitor:replies', args=(self.tweet.id,))
        response = self.client.get(url)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0].get('id'), self.response.id)

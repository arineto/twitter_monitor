from datetime import datetime
from django.test import TestCase
from django.urls import reverse
from model_mommy import mommy
from monitor.tests.utils.http_client_mixin import HTTPClientMixin
import mock
import pytz


class TestTweetListView(HTTPClientMixin, TestCase):

    def setUp(self):
        super(TestTweetListView, self).setUp()
        self.url = reverse('monitor:tweets')

        self.user1 = mommy.make('monitor.TwitterUser')
        self.user2 = mommy.make('monitor.TwitterUser')

        self.tweet1 = mommy.make(
            'monitor.Tweet', user=self.user1, text='test term 1',
            date=datetime(2017, 5, 25, 10, 10, 10, 0, pytz.UTC)
        )
        self.tweet2 = mommy.make(
            'monitor.Tweet', user=self.user1, text='test term 2',
            date=datetime(2017, 5, 26, 10, 10, 10, 0, pytz.UTC)
        )
        self.tweet3 = mommy.make(
            'monitor.Tweet', user=self.user2, text='trying term 3',
            date=datetime(2017, 5, 27, 10, 10, 10, 0, pytz.UTC)
        )

        self.hashtag = mommy.make('monitor.Hashtag', name='tag')
        self.tweet2.hashtags.add(self.hashtag)
        self.tweet3.hashtags.add(self.hashtag)

    def request(self, querystring):
        url = '{}?{}'.format(self.url, querystring)
        return self.client.get(url)

    def test_get(self):
        response = self.request('')
        self.assertEqual(len(response.data), 3)

        response = self.request('username={}'.format(self.user1.id))
        self.assertEqual(len(response.data), 2)

        response = self.request('term=test')
        self.assertEqual(len(response.data), 2)

        response = self.request('hashtags={}'.format(self.hashtag.id))
        self.assertEqual(len(response.data), 2)

        response = self.request('start_date=2017-05-26')
        self.assertEqual(len(response.data), 2)

        response = self.request('end_date=2017-05-26')
        self.assertEqual(len(response.data), 2)

        response = self.request('start_date=2017-05-26&end_date=2017-05-26')
        self.assertEqual(len(response.data), 1)


class TestTweetRetrieveView(HTTPClientMixin, TestCase):

    def setUp(self):
        super(TestTweetRetrieveView, self).setUp()
        self.tweet = mommy.make('monitor.Tweet')

    def test_get(self):
        url = reverse('monitor:tweet', args=(self.tweet.id,))
        response = self.client.get(url)
        self.assertEqual(response.data.get('id'), self.tweet.id)


class TestTweetReplyView(HTTPClientMixin, TestCase):

    def setUp(self):
        super(TestTweetReplyView, self).setUp()
        self.tweet = mommy.make('monitor.Tweet')

    def test_post(self):
        url = reverse('monitor:reply', args=(self.tweet.id,))

        with mock.patch('monitor.models.Tweet.reply', mock.Mock()) as reply:
            self.client.post(url, {'text': 'test'})
            reply.assert_called_with(self.auth_user, 'test')

from django.test import TestCase
from django.urls import reverse
from model_mommy import mommy
from monitor.tests.utils.http_client_mixin import HTTPClientMixin


class TestHashtagListView(HTTPClientMixin, TestCase):

    def setUp(self):
        super(TestHashtagListView, self).setUp()
        self.hashtags = mommy.make('monitor.Hashtag', _quantity=5)

    def test_get(self):
        url = reverse('monitor:hashtags')
        response = self.client.get(url)

        self.assertEqual(response.status_code, 200)

        for count, data in enumerate(response.data):
            self.assertTrue('id' in data.keys())
            self.assertTrue('name' in data.keys())
            self.assertEqual(data.get('id'), self.hashtags[count].id)
            self.assertEqual(data.get('name'), self.hashtags[count].name)

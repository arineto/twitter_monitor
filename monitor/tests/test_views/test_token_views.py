from django.test import TestCase
from django.urls import reverse
from monitor.tests.utils.http_client_mixin import HTTPClientMixin


class TestTokenRetrieveView(HTTPClientMixin, TestCase):

    def test_get(self):
        url = reverse('monitor:token')
        response = self.client.get(url)
        self.assertEqual(response.data.get('key'), self.token.key)

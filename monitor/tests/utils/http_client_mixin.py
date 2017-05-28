from django.test import Client
from model_mommy import mommy
from rest_framework.authtoken.models import Token


class HTTPClientMixin:

    def setUp(self):
        super(HTTPClientMixin, self).setUp()
        self.auth_user = mommy.make('users.User')
        self.token = Token.objects.create(user=self.auth_user)
        self.client = Client(
            HTTP_AUTHORIZATION='Token {}'.format(self.token.key)
        )

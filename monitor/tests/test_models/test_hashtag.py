from django.test import TestCase
from model_mommy import mommy


class TestHashtag(TestCase):

    def setUp(self):
        self.hashtag = mommy.make('monitor.Hashtag', name='test')

    def test__str__(self):
        self.assertEqual(str(self.hashtag), 'test')

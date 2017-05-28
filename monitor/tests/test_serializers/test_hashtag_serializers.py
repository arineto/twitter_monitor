from django.test import TestCase
from model_mommy import mommy
from monitor.api.serializers import HashtagSerializer


class TestHashtagSerializer(TestCase):

    def test_save(self):
        data = {'name': 'test'}
        serializer = HashtagSerializer(data=data)
        self.assertTrue(serializer.is_valid())

        instance = serializer.save()
        self.assertEqual(instance.name, data.get('name'))

    def test_dump(self):
        hashtag = mommy.make('monitor.Hashtag')
        serializer = HashtagSerializer(instance=hashtag)
        self.assertEqual(serializer.data.get('name'), hashtag.name)

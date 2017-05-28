from django.utils import timezone
from monitor.tests.utils.helpers import random_tweet
from random import randint
from tweepy.error import TweepError


class APIMock:

    def __init__(self, *args, **kwargs):
        super(APIMock, self).__init__()

    def get_user(self, username):
        return UserMock()

    def update_status(*args, **kwargs):
        return TweetMock('123')


class UserMock:

    def timeline(self, count):
        return [TweetMock(i) for i in range(5)]


class TweetMock:

    def __init__(self, tweet_id):
        self.id = tweet_id
        self.text = random_tweet
        self.created_at = timezone.now()
        self.entities = {
            'hashtags': [
                {'text': 'tag{}'.format(i)} for i in range(randint(0, 3))
            ]
        }


class APIMockError:

    def __init__(self, *args, **kwargs):
        super(APIMockError, self).__init__()

    def get_user(self, username):
        raise TweepError('')


class RequestMock:

    def __init__(self, user):
        self.user = user

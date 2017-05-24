from django.db import models
from monitor import enums
from tweepy.error import TweepError
from twitter_monitor.twitter_api import api


class TwitterUser(models.Model):

    user_id = models.CharField(max_length=20)

    username = models.CharField(max_length=100, unique=True)

    status = models.IntegerField(
        choices=enums.TWITTER_USER_STATUS_CHOICES,
        default=enums.TwitterUserStatusEnum.SEARCHING)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.username

    def update_status(self, status):
        self.status = status
        self.save()

    def retrieve_tweets(self):
        try:
            user = api.get_user(self.username)
            tweets = user.timeline(count=200)
            for tweet in tweets:
                Tweet.objects.create(
                    tweet_id=tweet.id, user=self, text=tweet.text,
                    date=tweet.created_at
                )
            self.update_status(enums.TwitterUserStatusEnum.VALID)
        except TweepError:
            self.update_status(enums.TwitterUserStatusEnum.INVALID)


class Tweet(models.Model):

    tweet_id = models.CharField(max_length=20)

    user = models.ForeignKey(TwitterUser)

    text = models.TextField(max_length=140)

    date = models.DateTimeField()

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return '{} - {}'.format(
            self.user, self.date.strftime('%d/%m/%Y %H:%I')
        )

    def reply(self, user, text):
        tweet = api.update_status(text, in_reply_to_status_id=self.tweet_id)
        TweetResponse.objects.create(
            response_id=tweet.id, user=user, tweet=self, text=text
        )


class TweetResponse(models.Model):

    response_id = models.CharField(max_length=20)

    user = models.ForeignKey('users.User')

    tweet = models.ForeignKey(Tweet)

    text = models.TextField(max_length=140)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return '{} ({})'.format(self.user, self.tweet)

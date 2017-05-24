from django.db import models
from monitor import enums


class TwitterUser(models.Model):

    username = models.CharField(max_length=100, unique=True)

    status = models.IntegerField(
        choices=enums.TWITTER_USER_STATUS_CHOICES,
        default=enums.TwitterUserStatusEnum.SEARCHING)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.username


class Tweet(models.Model):

    user = models.ForeignKey(TwitterUser)

    text = models.TextField(max_length=140)

    date = models.DateTimeField()

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return '{} - {}'.format(
            self.user, self.date.strftime('%d/%m/%Y %H:%I')
        )


class TweetResponse(models.Model):

    user = models.ForeignKey('users.User')

    tweet = models.ForeignKey(Tweet)

    text = models.TextField(max_length=140)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return '{} ({})'.format(self.user, self.tweet)

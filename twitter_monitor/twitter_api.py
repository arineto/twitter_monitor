from django.conf import settings
import tweepy


__all__ = ['get_api']


def get_api(key, secret):
    auth = tweepy.OAuthHandler(
        settings.SOCIAL_AUTH_TWITTER_KEY,
        settings.SOCIAL_AUTH_TWITTER_SECRET
    )
    auth.set_access_token(key, secret)
    return tweepy.API(auth)

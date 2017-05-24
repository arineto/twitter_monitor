from django.conf import settings
import tweepy

__all__ = ['api']

auth = tweepy.OAuthHandler(
    settings.SOCIAL_AUTH_TWITTER_KEY,
    settings.SOCIAL_AUTH_TWITTER_SECRET
)

auth.set_access_token(
    settings.SOCIAL_AUTH_TWITTER_ACCESS_TOKEN,
    settings.SOCIAL_AUTH_TWITTER_ACCESS_TOKEN_SECRET
)

api = tweepy.API(auth)

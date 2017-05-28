from twitter_monitor.celery import app
from monitor.models import TwitterUser
from users.models import User


@app.task
def retrieve_tweets(twitter_user_id, auth_user_id):
    auth_user = User.objects.get(id=auth_user_id)
    twitter_user = TwitterUser.objects.get(id=twitter_user_id)
    twitter_user.retrieve_tweets(auth_user)

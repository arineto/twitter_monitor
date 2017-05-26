from django.conf.urls import url
from monitor.api import views


urlpatterns = [
    url(r'token/$', views.TokenRetrieveView.as_view(), name='token'),
    url(r'users/$', views.TwitterUserView.as_view(), name='users'),
    url(r'tweets/$', views.TweetListView.as_view(), name='tweets'),
    url(r'usernames/$', views.UsernameListView.as_view(), name='usernames'),
    url(r'hashtags/$', views.HashtagListView.as_view(), name='hashtags'),
    url(r'tweet/(?P<pk>\d+)/$', views.TweetRetrieveView.as_view(),
        name='tweet'),
    url(r'reply/(?P<pk>\d+)/$', views.TweetReplyView.as_view(), name='reply'),
]

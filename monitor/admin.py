from django.contrib import admin
from monitor import models

# Register your models here.
admin.site.register(models.TwitterUser)
admin.site.register(models.Tweet)
admin.site.register(models.TweetResponse)
admin.site.register(models.Hashtag)

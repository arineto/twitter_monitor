class TwitterUserStatusEnum:

    SEARCHING = 0
    VALID = 1
    INVALID = 2


TWITTER_USER_STATUS_CHOICES = (
    (TwitterUserStatusEnum.SEARCHING, 'Searching'),
    (TwitterUserStatusEnum.VALID, 'Valid'),
    (TwitterUserStatusEnum.INVALID, 'Invalid'),
)

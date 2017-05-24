import random


def random_tweet():
    original_text = '1234567890abcdefghijklmnopqstuwxyz'
    return ''.join(random.choice(original_text) for _ in range(140))

web: gunicorn twitter_monitor.wsgi --limit-request-line 8188 --log-file -
worker: celery worker --app=twitter_monitor --loglevel=info

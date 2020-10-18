from __future__ import absolute_import
import os
from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'assignment2.settings')

app = Celery('assignment2')

app.config_from_object('django.conf:settings', namespace='CELERY')

app.autodiscover_tasks()


@app.task(bind=True)
def debug_task(self):
    print('Request: {0!r}'.format(self.request))


app.conf.beat_schedule = {
    'fetch-periodically': {
        'task': 'fetch_latest_videos',
        'schedule': 30.0,
        'args': ('party',),
    }
}

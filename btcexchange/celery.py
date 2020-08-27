from __future__ import absolute_import, unicode_literals

from celery import Celery
from django.conf import settings

import os
from celery.task import periodic_task as p_task

settings_module = os.environ.get('DJANGO_SETTINGS_MODULE', None)

if not settings_module:
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'btcexchange.settings')
app = Celery("btcexchange")
app.config_from_object("django.conf:settings", namespace="CELERY")
app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)



@app.task(bind=True)
def debug_task(self):
    print('Request: {0!r}'.format(self.request))


# Custom Tasks
AUTO_RETRY_TASK_EXCEPTIONS = (Exception,)


def task(*args, **opts):
    return app.task(
        *args,
        autoretry_for=AUTO_RETRY_TASK_EXCEPTIONS,
        **opts
    )


def periodic_task(*args, **opts):
    return p_task(
        *args,
        autoretry_for=AUTO_RETRY_TASK_EXCEPTIONS,
        **opts
    )


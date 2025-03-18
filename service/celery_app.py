import os
import time
from celery import Celery
from django.conf import settings

os.environ.setdefault('DJANGO_SETTINGS_MODULE','service.settings')

app=Celery('service') #proj_name
app.config_from_object('django.conf:settings')#настройки из django.settings
app.conf.broker_url=settings.CELERY_BROKER_URL #брокером будет redis
app.autodiscover_tasks() #чтобы celery искал по проекту таски

@app.task()
def debug_tasks():
    time.sleep(20)
    print('Hello from debug task')

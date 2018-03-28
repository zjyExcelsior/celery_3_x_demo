# coding=utf-8
from celery import Celery

app = Celery('celery_3_x_demo',
             broker='amqp://guest:guest@localhost:5672/celery_3_x_demo',
             backend='rpc://guest:guest@localhost:5672/celery_3_x_demo',
             include=['celery_3_x_demo.tasks'])

app.conf.update(
    CELERY_TASK_RESULT_EXPIRES=3600
)

# coding=utf-8
from celery import Celery

app = Celery('celery_3_x_demo', broker='amqp://', backend='amqp://',
             include=['celery_3_x_demo.tasks'])

app.conf.update(
    CELERY_TASK_RESULT_EXPIRES=3600
)

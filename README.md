# celery_3_x_demo

启动 celery worker:

    $ celery worker --app=celery_3_x_demo.celery_app --concurrency=4 -Ofair --loglevel=info

测试：

    $ python test_tasks.py

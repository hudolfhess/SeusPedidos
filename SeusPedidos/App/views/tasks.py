from celery.decorators import task
from SeusPedidos.celery_tasks import app as app_celery
import time


@task
def send_email(x):
    print '===aaa==='
    time.sleep(x)
    print '===bbb==='

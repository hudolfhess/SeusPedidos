from __future__ import absolute_import
from celery import Celery
from django.conf import settings
import os
import time

# set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'SeusPedidos.settings')
app = Celery(
    'SeusPedidos',
    broker='redis://localhost:6379/0',
    backend='redis://localhost:6379/0',
    include=['SeusPedidos.App.views.tasks.send_email']
)


'''
BROKER_URL = 'redis://localhost:6379/0'
CELERY_RESULT_BACKEND = 'redis://localhost:6379/0'

celery = Celery('representante',
                broker=redis_fqdn,
                backend=redis_fqdn,
                include=['pedidos.tasks',
                         'vendas.tasks',
                         'vendas.tasks_agendadas',
                         'empresas.tasks',
                         'vendas.fluxo_onboard_tasks',
                         'integracoes.tasks',
                         'api.tasks',
                         'tasks_celery',
                         ])

# Using a string here means the worker will not have to
# pickle the object when using Windows.
app.config_from_object('django.conf:settings')
app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)

@app.task(name="send_email")
def send_email(x):
    print '===aaa==='
    time.sleep(x)
    print '===bbb==='
    return True
'''

if __name__ == '__main__':
    app.start()
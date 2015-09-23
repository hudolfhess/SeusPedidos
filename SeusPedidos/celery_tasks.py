from __future__ import absolute_import
from celery import Celery

app = Celery(
    'SeusPedidosWorker',
    broker='redis://localhost:6379/0',
    backend='redis://localhost:6379/0',
    include=['SeusPedidos.App.celery.send_email']
)

if __name__ == '__main__':
    app.start()
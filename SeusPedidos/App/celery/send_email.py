from celery.decorators import task
from django.core.mail import send_mail


@task
def send_email(subject, message, customer_email):
    send_mail(
        subject,
        message,
        'hudolf@gmail.com',
        [
            customer_email
        ],
        fail_silently=False
    )

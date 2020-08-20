from celery import task
from django.core.mail import send_mail

from .models import Order

@task
def order_created(order_id):
    order = Order.objects.get(id=order_id)
    send_mail(
        'Заказ оформлен',
        'Спасибо за заказ! Номер заказа {}'.format(order.id),
        'bohdangavryschuk@gmail.com',
        [order.email],
        fail_silently=False,
    )
import string

from django.contrib.auth.models import User
from django.utils.crypto import get_random_string
#timezone
from django.utils import timezone

from celery import shared_task
from .send_mail import send_mail



@shared_task
def create_random_user_accounts(total):
    for i in range(total):
        username = 'user_{}'.format(get_random_string(10, string.ascii_letters))
        email = '{}@example.com'.format(username)
        password = get_random_string(50) # delay
        User.objects.create_user(username=username, email=email, password=password)
    return '{} random users created with success!'.format(total)


@shared_task
def send_to_users(email, title, body):
    return send_mail(email, title, body)


@shared_task
def send_to_user(user_id):
    user = User.objects.get(id=user_id)


@shared_task
def send_mail_task():
    users = User.objects.filter(is_staff=True)
    for user in users:
        send_to_users(user.email, 'Отчет за неделю', f'{user.first_name} ты забыл отправить отчет {timezone.now()}')
    return 'Отчет просрочкуи для админа!'


# @shared_task
# def send_mail_task():
#     users = User.objects.filter(is_admin=True)
#     for user in users:
#         send_to_users(user.email, 'Отчет за неделю', f'{user.first_name} ты забыл отправить отчет {timezone.now()}')
#     return 'Отчет просрочкуи для админа!'




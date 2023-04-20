import os
from celery import Celery
from celery.schedules import crontab
import blog 

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'sinema.settings')

app = Celery('sinema')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()
app.conf.timezone = 'Asia/Bishkek'


app.conf.beat_schedule = {
    'add-every-5-seconds': {
        'task': 'blog.tasks.send_mail_task',
        'schedule': crontab(minute='*/1'), # crontab(0, 0, day_of_month='22')
        'args': ()
    },
}


@app.on_after_configure.connect
def setup_periodic_tasks(sender, **kwargs):
    # Calls test('hello') every 10 seconds.
    sender.add_periodic_task(10.0, blog.tasks.create_random_user_accounts.s('14'), name='add every 10')


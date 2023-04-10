shell ORM
python3 manage.py shell 


# Мы можем получать так все данные

-> from blog.models import Cinema
-> Cinema.object.all()


pip install ipython - [SQL comand's]
python3 manage.py dbshell

______________________________________________________________________________
shell - create 
if models -> DateTimeField -> write from datetime import datetime   
                           -> now = datetime.now()
                                    from django.utils import timezone 
                           -> now = timezone.now()

from django.contrib.auth.models import User 

[Если в моделс есть - auto_now_add=True, то можно не писать]

-> Cinema.objects.create(name='Мстители', duration=154, title='Эра возме
    ...: здия', image='django_sinema/media/avengers.jpg', rental_start_date=no
    ...: w, rental_finish_date=now, sales_company='ITC_bootcamp',author=User.o
    ...: bjects.get(id=1))
______________________________________________________________________________
shell update 

[Нужно испортировать тот модель, которую хочешь изменить] - Example "from blog.models import your_model"

Cinema.objects.filter(id=1).update(name='Мстители. Эра Альтрона')
_______________________________________________________________________________



5 or 4 exaample
sessions.objects.get(id=3)

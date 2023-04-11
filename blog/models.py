from django.db import models
from django.contrib.auth.models import User 

# Create your models here.


class Cinema(models.Model):
    name = models.CharField(max_length=50, verbose_name='Название')
    duration = models.CharField(max_length=25, verbose_name='Длительность')
    title = models.CharField(max_length=250, verbose_name='Описание')
    image = models.ImageField(null=True, blank=True)  
    rental_start_date = models.DateTimeField(verbose_name='Дата начало проката')
    rental_finish_date = models.DateTimeField(verbose_name='Дата окончания проката') 
    sales_company = models.CharField(max_length=50, verbose_name='Название компании')
    date_pub = models.DateTimeField(auto_now_add=True, verbose_name='Дата публикации') 
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Автор', null=True, blank=True)

    def __str__(self): # Будет показывать имя в Админке
        return self.name 
    
    class Meta:
        verbose_name = 'Фильм'
        verbose_name_plural = 'Фильмы'
        ordering = ['-date_pub']


class Saloon(models.Model):
    name = models.CharField(max_length=50, verbose_name='Залы')
    count_place = models.IntegerField(verbose_name='Колличество мест')
    description = models.CharField(max_length=100, verbose_name='Описание зала')
    number_of_rows = models.IntegerField(verbose_name='Число рядов')
    number_of_places = models.IntegerField(verbose_name='Число мест')

    class Meta:
        verbose_name = 'Зал'
        verbose_name_plural = 'Залы'
        ordering = ['name']

    def __str__(self):
        return self.name
    


class Sector_salon(models.Model):
    sector_salon = models.ForeignKey(Saloon, on_delete=models.CASCADE, verbose_name='Секторы зала', related_name='sector_salon')
    name = models.CharField(max_length=50, verbose_name='Секторы зала')
    description = models.CharField(max_length=100, verbose_name='Описание секторов зала')

    class Meta:
        verbose_name = 'Сектор зала'
        verbose_name_plural = 'Секторы зала'
        ordering = ['name']

    def __str__(self):
        return self.name


class Seanses(models.Model):
    seanses = models.ForeignKey(Saloon, on_delete=models.CASCADE, verbose_name='Сеансы', related_name='seanses')
    date = models.DateTimeField(verbose_name='Дата')
    time = models.TimeField(verbose_name='Время')
    movie = models.ForeignKey(Cinema, on_delete=models.CASCADE, verbose_name='Фильм', related_name='movie_seanses')

    class Meta:
        verbose_name = 'Сеанс'
        verbose_name_plural = 'Сеансы'
        ordering = ['movie']

    def __str__(self):
        return str(self.seanses)


class Places(models.Model):
    places = models.ForeignKey(Saloon, on_delete=models.CASCADE, verbose_name='Места', related_name='places')
    row_number = models.IntegerField(verbose_name='Номер ряда')
    row_place = models.IntegerField(verbose_name='Номер места')

    class Meta:
        verbose_name = 'Место'
        verbose_name_plural = 'Места'
        ordering = ['places']

    def __str__(self):
        return str(f'{self.places}')


class Price_for_tickets(models.Model):
    price_for_ticket = models.ForeignKey(Seanses, on_delete=models.CASCADE, verbose_name='Стоимость билета', related_name='price_for_ticket')
    sector = models.ForeignKey(Sector_salon, on_delete=models.CASCADE, verbose_name='Сектор', related_name='sector')
    price = models.IntegerField(verbose_name='Цена')

    class Meta:
        verbose_name = 'Стоимость билета'
        verbose_name_plural = 'Стоимость билетов'
        ordering = ['price_for_ticket'] 

    def __str__(self):
        return f'Price={self.price_for_ticket}, Sector={self.sector}'


class Tickets(models.Model):
    ticket_number = models.IntegerField(verbose_name='Номер билета')
    date_created = models.DateTimeField(verbose_name='Дата печати билета')
    seans = models.ForeignKey(Seanses, on_delete=models.CASCADE, verbose_name='Сеанс', related_name='seans')
    place = models.ForeignKey(Places, on_delete=models.CASCADE, verbose_name='Место', related_name='place')
    payed = models.BooleanField(verbose_name='Оплачено')
    booking = models.BooleanField(verbose_name='Забронирован')
    crashed = models.BooleanField(verbose_name='Утилизирован')

    class Meta:
        verbose_name = 'Билет'
        verbose_name_plural = 'Билеты'
        ordering = ['ticket_number'] 

    def __str__(self):
        return str(self.ticket_number)


class JobTitle(models.Model):
    title = models.CharField(max_length=250, verbose_name='Информация')

    class Meta:
        verbose_name = 'Должность'
        verbose_name_plural = 'Должности'
        ordering = ['title']

    def __str__(self):
        return str(self.title)
    

class Employees(models.Model):
    name = models.CharField(max_length=75, verbose_name='ФИО')
    title = models.ForeignKey(JobTitle, on_delete=models.CASCADE, verbose_name='Описание', related_name='employees')
    password = models.CharField(max_length=50, verbose_name='Пароль')

    class Meta:
        verbose_name = 'Сотрудник'
        verbose_name_plural = 'Сотрудники'
        ordering = ['name']    

    def __str__(self):
        return str(self.name)


class Moving_tickets(models.Model):
    number_ticket = models.ForeignKey(Tickets, on_delete=models.CASCADE, verbose_name='Билет номер', related_name='number_ticket')
    date = models.DateTimeField(verbose_name='Дата')
    operation = models.CharField(max_length=50, verbose_name='Операции')
    employee = models.ForeignKey(Employees, on_delete=models.CASCADE, verbose_name='Сотрудник', related_name='employee')
    seller = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Продавец', related_name='seller')

    def __str__(self):
        return f"{str(self.number_ticket)}, {str(self.employee)}"

    class Meta:
        verbose_name = 'Движение билета'
        verbose_name_plural = 'Движение билетов'
        ordering = ['number_ticket'] 


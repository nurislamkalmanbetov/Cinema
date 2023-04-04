from django.shortcuts import render
from django.http import HttpResponse
from .models import *

from rest_framework.generics import ListAPIView, CreateAPIView
from rest_framework import filters
from .serializers import *
import django_filters

class CinemaListAPIView(ListAPIView):
    serializer_class = CinemaSerializers
    filter_backends = {filters.SearchFilter, filters.OrderingFilter, django_filters.rest_framework.DjangoFilterBackend}
    # filterset_fields = ('sales_company') # то что нужно, фронтендер будет запрашивать и только это нужно

    def get_queryset(self):

        queryset = Cinema.objects.all()
        return queryset
    

class SaloonListAPIView(ListAPIView):
    serializer_class = SaloonSerializers
    filter_backends = {filters.SearchFilter, filters.OrderingFilter, django_filters.rest_framework.DjangoFilterBackend}
    # то что нужно, фронтендер будет запрашивать и только это нужно

    def get_queryset(self):

        queryset = Saloon.objects.all()
        return queryset
    

class Sector_salonListAPIView(ListAPIView):
    serializer_class = Sector_salonSerializers
    filter_backends = {filters.SearchFilter, filters.OrderingFilter, django_filters.rest_framework.DjangoFilterBackend}

    def get_queryset(self):
        queryset = Sector_salon.objects.all()
        return queryset


class JobtitleListAPIView(ListAPIView):
    serializer_class = JobTitleSerializers
    filter_backends = {filters.SearchFilter, filters.OrderingFilter, django_filters.rest_framework.DjangoFilterBackend}

    def get_queryset(self):
        queryset = JobTitle.objects.all()
        return queryset   
    

class EmployeesListAPIView(ListAPIView):
    serializer_class = EmployeesSerializers
    filter_backends = {filters.SearchFilter, filters.OrderingFilter, django_filters.rest_framework.DjangoFilterBackend}
    filterset_fields = ('title__title',)

    def get_queryset(self):
        queryset = Employees.objects.all()
        return queryset  
    

class EmployeeCreateAPIView(CreateAPIView):
    serializer_class = EmployeesSerializers
    queryset = Employees.objects.all()















# Create your views here.

# def index(request):
#     return HttpResponse("Привет! Моя первая страница")

# def get_movies(request):
#     cinemas = Cinema.objects.all() 
#     result = ''
#     for cinema in cinemas:
#         result += f'{cinema.image} {cinema.name} {cinema.duration} {cinema.rental_start_date} <br><br>'
#     return HttpResponse(result)

# def get_employee(request):
#     employees = Employees.objects.all()
#     result = ''
#     for employee in employees:
#         result += f'{employee.name} {employee.title.title} <br><br>'
#     return HttpResponse(result)

# def get_saloon(request):
#     saloons = Saloon.objects.all()
#     result = ''
#     for saloon in saloons:
#         result += f'{saloon.name} {saloon.count_place} {saloon.description} {saloon.number_of_rows} {saloon.number_of_places} <br><br>'
#     return HttpResponse(result)

# def get_sector_saloon(request):
#     sector_saloons = Sector_salon.objects.all()
#     result = ''
#     for sector_saloon in sector_saloons:
#         result += f'{sector_saloon.sector_salon.name} {sector_saloon.name} {sector_saloon.name} {sector_saloon.description} <br><br>'
#     return HttpResponse(result)   

# def get_seanses(request):
#     seanses = Seanses.objects.all()
#     result = ''
#     for seans in seanses:
#         result += f'{seans.seanses.name} {seans.date} {seans.time} {seans.movie.name} <br><br>' 
#     return HttpResponse(result) 

# def get_places(request):
#     places = Places.objects.all()
#     result = ''
#     for place in places:
#         result += f'{place.places.name} {place.row_number} {place.row_place} <br><br>'
#     return HttpResponse(result) 

# def get_price_for_ticket(request):
#     price_for_tickets = Price_for_tickets.objects.all()
#     result = ''
#     for price_for_ticket in price_for_tickets:
#         result += f'{price_for_ticket.price_for_ticket.seanses} {price_for_ticket.sector.sector_salon.name} {price_for_ticket.price} <br><br>'
#     return HttpResponse(result) 

# def get_tickets(request):
#     tickets = Tickets.objects.all()
#     result = ''
#     for ticket in tickets:
#         result += f'{ticket.ticket_number} {ticket.date_created} {ticket.seans.seanses.name} {ticket.place.places.name} {ticket.payed} {ticket.booking} {ticket.crashed} <br><br>'
#     return HttpResponse(result) 

# def get_jobtitle(request):
#     job_titles = JobTitle.objects.all()
#     result = ''
#     for job_title in job_titles:
#         result += f'{job_title.title}  <br><br>'
#     return HttpResponse(result) 

# def get_moving_tickets(request):
#     moving_tickets = Moving_tickets.objects.all()
#     result = ''
#     for moving_ticket in moving_tickets:
#         result += f'{moving_ticket.number_ticket.ticket_number} {moving_ticket.date} {moving_ticket.operation} {moving_ticket.employee.name} <br><br>'
#     return HttpResponse(result) 
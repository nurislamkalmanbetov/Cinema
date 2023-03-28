from django.contrib import admin
from .models import *

# Register your models here.


class CinemaAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'duration', 'rental_start_date', 'rental_finish_date', 'sales_company', 'date_pub', 'author')
    list_display_links = ('id', 'name') # кликабельные столбцы, при клике будут доступны
    search_fields = ('name', 'title')
    list_filter = ('date_pub', )


class SaloonAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'description')
    list_display_links = ('id', 'name') # кликабельные столбцы, при клике будут доступны
    search_fields = ('name', 'description')
    list_filter = ('name', )


class Sector_salonAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'description')
    list_display_links = ('id', 'name') # кликабельные столбцы, при клике будут доступны
    search_fields = ('name', 'description')
    list_filter = ('name', )


class SeansesAdmin(admin.ModelAdmin):
    list_display = ('id', 'seanses', 'date', 'time', 'movie')
    list_display_links = ('seanses', 'movie') # кликабельные столбцы, при клике будут доступны
    search_fields = ('seanses', 'movie')
    list_filter = ('movie', )


class PlacesAdmin(admin.ModelAdmin):
    list_display = ('id', 'places', 'row_number', 'row_place')
    list_filter = ('places', )


class Price_for_ticketsAdmin(admin.ModelAdmin):
    list_display = ('id', 'price_for_ticket', 'sector', 'price')
    list_filter = ('sector', )       


class TicketsAdmin(admin.ModelAdmin):
    list_display = ('ticket_number', 'date_created', 'seans', 'place', 'payed', 'booking', 'crashed')
    list_display_links = ('seans', 'payed', 'booking', 'crashed') # кликабельные столбцы, при клике будут доступны
    search_fields = ('ticket_number', 'date_created')
    list_filter = ('ticket_number', ) 


class Moving_ticketsAdmin(admin.ModelAdmin):
    list_display = ('id', 'number_ticket', 'date', 'operation', 'employee')
    list_display_links = ('number_ticket', 'operation', 'employee') # кликабельные столбцы, при клике будут доступны
    search_fields = ('number_ticket', 'date')
    list_filter = ('number_ticket', ) 


class EmployeesAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'title', 'password')
    list_display_links = ('name', 'title', 'password') # кликабельные столбцы, при клике будут доступны
    search_fields = ('name', 'title')
    list_filter = ('name', )     


class Job_titleAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')
    list_display_links = ('title',) # кликабельные столбцы, при клике будут доступны
    search_fields = ('title',)
    list_filter = ('title', )     


admin.site.register(Cinema, CinemaAdmin)
admin.site.register(Saloon, SaloonAdmin)
admin.site.register(Sector_salon, Sector_salonAdmin)
admin.site.register(Seanses, SeansesAdmin)
admin.site.register(Places, PlacesAdmin)
admin.site.register(Price_for_tickets, Price_for_ticketsAdmin)
admin.site.register(Tickets, TicketsAdmin)
admin.site.register(Moving_tickets, Moving_ticketsAdmin)
admin.site.register(Employees, EmployeesAdmin)
admin.site.register(Job_title, Job_titleAdmin)
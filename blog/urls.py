from django.urls import path
from . import views


urlpatterns = [
    path('firsturl/', view=views.index, name='index'),
    path('movies/', view=views.get_movies, name='movies'),
    path('employees/', view=views.get_employee, name='employees'),
    path('saloons/', view=views.get_saloon, name='saloons'),
    path('sectorsaloons/', view=views.get_sector_saloon, name='sectorsaloons'),
    path('seanses/', view=views.get_seanses, name='index'),
    path('places/', view=views.get_places, name='places'),
    path('pricefortickets/', view=views.get_price_for_ticket, name='pricefortickets'),
    path('tickets/', view=views.get_tickets, name='tickets'),
    path('jobtitles/', view=views.get_jobtitle, name='jobtitles'),
    path('movingtickets/', view=views.get_moving_tickets, name='movingtickets')
]
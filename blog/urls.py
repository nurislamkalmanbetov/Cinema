from django.urls import path
from .views import CinemaListAPIView, SaloonListAPIView, Sector_salonListAPIView, JobtitleListAPIView, EmployeesListAPIView, EmployeeCreateAPIView


urlpatterns = [
    path('cinema/', CinemaListAPIView.as_view()),
    path('saloon/', SaloonListAPIView.as_view()),
    path('sectorsalon/', Sector_salonListAPIView.as_view()),
    path('jobtitle/', JobtitleListAPIView.as_view()),
    path('employees/', EmployeesListAPIView.as_view()),
    path('employees/create/', EmployeeCreateAPIView.as_view()),
]


# urlpatterns = [
#     path('firsturl/', view=views.index, name='index'),
#     path('movies/', view=views.get_movies, name='movies'),
#     path('employees/', view=views.get_employee, name='employees'),
#     path('saloons/', view=views.get_saloon, name='saloons'),
#     path('sectorsaloons/', view=views.get_sector_saloon, name='sectorsaloons'),
#     path('seanses/', view=views.get_seanses, name='index'),
#     path('places/', view=views.get_places, name='places'),
#     path('pricefortickets/', view=views.get_price_for_ticket, name='pricefortickets'),
#     path('tickets/', view=views.get_tickets, name='tickets'),
#     path('jobtitles/', view=views.get_jobtitle, name='jobtitles'),
#     path('movingtickets/', view=views.get_moving_tickets, name='movingtickets')
# ]
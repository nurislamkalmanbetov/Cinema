from django.urls import path
from .views import *


urlpatterns = [
    path('cinema/', CinemaListAPIView.as_view()),
    path('cinema/post', CinemaCreateAPIView.as_view()),
    path('cinema/<int:pk>/', CinemaRetriveAPIView.as_view(), name='cinema_retrieve'),
    path('cinema/delete/<int:pk>/', CinemaDestroyAPIView.as_view(), name='cinema_delete'),
    path('cinema/update<int:pk>/', CinemaUpdateAPIView.as_view(), name='cinema_update'),
    
    path('seanses/', SeansesListAPIView.as_view()),
    path('seanses/post', SeansesCreateAPIView.as_view()),
    path('seanses/<int:pk>/', SeansesRetriveAPIView.as_view(), name='seanses_retrieve'),
    path('seanses/delete/<int:pk>/', SeansesDestroyAPIView.as_view(), name='seanses_delete'),
    path('seanses/update/<int:pk>/', SeansesUpdateAPIView.as_view(), name='seanses_update'),

    path('saloon/', SaloonListAPIView.as_view()),
    path('saloon/post', SaloonCreateAPIView.as_view()),
    path('saloon/<int:pk>/', SaloonRetriveAPIView.as_view(), name='saloon_retrieve'),
    path('saloon/delete/<int:pk>/', SaloonDestroyAPIView.as_view(), name='saloon_delete'),
    path('saloon/update/<int:pk>/', SaloonUpdateAPIView.as_view(), name='saloon_update'),

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
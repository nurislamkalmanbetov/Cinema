from django.urls import path
from .views import *
from rest_framework.authtoken import views 


urlpatterns = [
    # authtokem
    path('api-token-auth/', AuthTokenView.as_view(), name='api_token_auth'),
    #user
    path('registration/', RegistrationView.as_view(), name='registration'),
    # Cinema
    path('cinema/', CinemaListAPIView.as_view(), name='cinema'),
    path('cinema/post', CinemaCreateAPIView.as_view()),
    path('cinema/<int:pk>/', CinemaRetriveAPIView.as_view(), name='cinema_retrieve'),
    path('cinema/delete/<int:pk>/', CinemaDestroyAPIView.as_view(), name='cinema_delete'),
    path('cinema/update<int:pk>/', CinemaUpdateAPIView.as_view(), name='cinema_update'),
    # Sinema
    path('seanses/', SeansesListAPIView.as_view()),
    path('seanses/post', SeansesCreateAPIView.as_view()),
    path('seanses/<int:pk>/', SeansesRetriveAPIView.as_view(), name='seanses_retrieve'),
    path('seanses/delete/<int:pk>/', SeansesDestroyAPIView.as_view(), name='seanses_delete'),
    path('seanses/update/<int:pk>/', SeansesUpdateAPIView.as_view(), name='seanses_update'),
    # Saloon
    path('saloon/', SaloonListAPIView.as_view()),
    path('saloon/post', SaloonCreateAPIView.as_view()),
    path('saloon/<int:pk>/', SaloonRetriveAPIView.as_view(), name='saloon_retrieve'),
    path('saloon/delete/<int:pk>/', SaloonDestroyAPIView.as_view(), name='saloon_delete'),
    path('saloon/update/<int:pk>/', SaloonUpdateAPIView.as_view(), name='saloon_update'),
    # Moving tickets
    path('moving_tickets/', MovingTicketsListCreateAPIView.as_view(), name='moving_tickets_list_create'),
    path('moving_tickets/<int:pk>/', MovingTicketsRetrieveUpdateDestroyAPIView.as_view(), name='moving_tickets_retrieve_update_destroy'),
 

    path('sectorsalon/', Sector_salonListAPIView.as_view()),
    path('jobtitle/', JobtitleListAPIView.as_view()),
    path('employees/', EmployeesListAPIView.as_view()),
    path('employees/create/', EmployeeCreateAPIView.as_view()),
    #TemplateView
    path('cinema_template/', CinemaTemplateView.as_view(), name='cinema_template'),
    path('cinema_detail/<int:pk>/', CinemaDetailView.as_view(), name='cinema_detail'),
    path('cinema_create/', CinemaCreateView.as_view(), name='cinema_create'),
    #Celery
    path('users_list/', GenerateRandomUserView.as_view(), name='users_list'),


    # path('', TemplateView.as_view(template_name='base.html'), name='base')
    # path('getmovie/', get_movies, name='getmovie'),
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
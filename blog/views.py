from django.shortcuts import render
from django.http import HttpResponse
from .models import *

from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveAPIView, DestroyAPIView, UpdateAPIView, ListCreateAPIView
from rest_framework import filters
from .serializers import *
import django_filters

from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly



# auth
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.response import Response 


class AuthTokenView(ObtainAuthToken):
    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data, context={'request': request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)
        return Response({
            'token': token.key,
            'user_id': user.pk,
            'email': user.email,
            'name': user.first_name
        })




# _________________________________________________________________________________________________
# Cinema - ListAPIView, CreateAPIView, Filter(django_filters.FilterSet), RetrieveAPIView, DestroyAPIView,


class CinemaFilter(django_filters.FilterSet):
    start_year = django_filters.NumberFilter(field_name='rental_start_date__year') # + __year # + NumberFilter
    class Meta:
        model = Cinema
        fields = ('start_year', )


class CinemaListAPIView(ListAPIView):
    serializer_class = CinemaSerializers
    filter_backends = {filters.SearchFilter, filters.OrderingFilter, django_filters.rest_framework.DjangoFilterBackend}
    # filterset_fields = ('sales_company', ) # то что нужно, фронтендер будет запрашивать и только это нужно
    search_fields = ('name', 'sales_company')
    # filterset_class = CinemaFilter

    def get_queryset(self):
        queryset = Cinema.objects.all()
        # queryset = Cinema.objects.filter(rental_start_date__year=year) == MovieFilter.start_date
        return queryset
    
    
class CinemaCreateAPIView(CreateAPIView): # Может создавать новые данные фронтендер через swagger
    serializer_class = CinemaSerializers    
    
    def get_queryset(self):
        queryset = Cinema.objects.all()
        return queryset


class CinemaRetriveAPIView(RetrieveAPIView): # фронтендеру поиск по ID
    serializer_class = CinemaDetailSerializer
    queryset = Cinema.objects.all()


class CinemaDestroyAPIView(DestroyAPIView):
    serializer_class = CinemaDetailSerializer
    queryset = Cinema.objects.all()


class CinemaUpdateAPIView(UpdateAPIView):
    serializer_class = CinemaDetailSerializer
    queryset = Cinema.objects.all()

# _________________________________________________________________________________________________

# Seanses - ListAPIView, CreateAPIView, Filter(django_filters.FilterSet), RetrieveAPIView, DestroyAPIView,

class SeansesFilter(django_filters.FilterSet):
    date = django_filters.DateTimeFilter(field_name='date', lookup_expr='date') # + __year # + NumberFilter \ lookup_expr = делит дату
    
    class Meta:
        model = Seanses
        fields = ('date', )


class SeansesListAPIView(ListCreateAPIView):
    serializer_class = SeansesSerializers
    queryset = Seanses.objects.all()
    filter_backends = {filters.SearchFilter, filters.OrderingFilter, django_filters.rest_framework.DjangoFilterBackend}
    filterset_class = SeansesFilter # то что нужно, фронтендер будет запрашивать и только это нужно
    search_fields = ('seanses', 'date', 'time', 'movie')

    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticatedOrReadOnly]

    # def get_queryset(self):
    #     queryset = Seanses.objects.all()
    #     return queryset


class SeansesCreateAPIView(CreateAPIView): # Может создавать новые данные фронтендер через swagger
    serializer_class = SeansesSerializers    
    
    def get_queryset(self):
        queryset = Seanses.objects.all()
        return queryset
    

class SeansesRetriveAPIView(RetrieveAPIView): # фронтендеру поиск по ID
    serializer_class = SeansesDetailSerializer
    queryset = Seanses.objects.all()


class SeansesDestroyAPIView(DestroyAPIView):
    serializer_class = SeansesDetailSerializer
    queryset = Seanses.objects.all()


class SeansesUpdateAPIView(UpdateAPIView):
    serializer_class = SeansesDetailSerializer
    queryset = Seanses.objects.all()


# _________________________________________________________________________________________________
# Saloon - ListAPIView, CreateAPIView, Filter(django_filters.FilterSet), RetrieveAPIView, DestroyAPIView,

class SaloonListAPIView(ListAPIView):
    serializer_class = SaloonSerializers
    filter_backends = {filters.SearchFilter, filters.OrderingFilter, django_filters.rest_framework.DjangoFilterBackend}
    # то что нужно, фронтендер будет запрашивать и только это нужно

    def get_queryset(self):

        queryset = Saloon.objects.all()
        return queryset


class SaloonCreateAPIView(CreateAPIView): # Может создавать новые данные фронтендер через swagger
    serializer_class = SaloonSerializers    
    
    def get_queryset(self):
        queryset = Saloon.objects.all()
        return queryset


class SaloonRetriveAPIView(RetrieveAPIView): # фронтендеру поиск по ID
    serializer_class = SaloonDetailSerializer
    queryset = Saloon.objects.all()


class SaloonDestroyAPIView(DestroyAPIView):
    serializer_class = SaloonDetailSerializer
    queryset = Saloon.objects.all()


class SaloonUpdateAPIView(UpdateAPIView):
    serializer_class = SaloonDetailSerializer
    queryset = Saloon.objects.all()

# _________________________________________________________________________________________________
# Sector - ListAPIView, CreateAPIView, Filter(django_filters.FilterSet), RetrieveAPIView, DestroyAPIView, 


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
    search_fields = ('name', 'title', 'password', )

    def get_queryset(self):
        queryset = Employees.objects.all()
        return queryset  
    

class EmployeeCreateAPIView(CreateAPIView):
    serializer_class = EmployeesSerializers
    queryset = Employees.objects.all()

    def get_queryset(self):
        queryset = Employees.objects.all()
        return queryset















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


from django.shortcuts import render
from django.http import HttpResponse
from .models import *
# templates
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView
from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView
from django.urls import reverse
from .forms import *



from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveAPIView, DestroyAPIView, UpdateAPIView, ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework import generics, filters, status
from .serializers import *
import django_filters

#auth
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly

# auth
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.response import Response 

#user
from django.contrib.auth.models import User

from rest_framework.permissions import DjangoModelPermissionsOrAnonReadOnly




class RegistrationView(CreateAPIView):
    serializer_class = UserRegistrationSerializers
    
    
    def post(self, request, *args, **kwargs):
        serializer = UserRegistrationSerializers(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = User.objects.create_user(username=serializer.validated_data['username'], password=serializer.validated_data['password'])
        token, created = Token.objects.get_or_create(user=user)
        return Response({
                'username': user.username,
                'token': token.key
            }
        )

#_______________________________________________________________________________________________

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

    permission_classes = [DjangoModelPermissionsOrAnonReadOnly]


class CinemaListAPIView(ListAPIView):
    serializer_class = CinemaSerializers
    filter_backends = {filters.SearchFilter, filters.OrderingFilter, django_filters.rest_framework.DjangoFilterBackend}
    # filterset_fields = ('sales_company', ) # то что нужно, фронтендер будет запрашивать и только это нужно
    search_fields = ('name', 'sales_company')
    # filterset_class = CinemaFilter
    permission_classes = [DjangoModelPermissionsOrAnonReadOnly]


    def get_queryset(self):
        queryset = Cinema.objects.all()
        # queryset = Cinema.objects.filter(rental_start_date__year=year) == MovieFilter.start_date
        return queryset
    
    
class CinemaCreateAPIView(CreateAPIView): # Может создавать новые данные фронтендер через swagger
    serializer_class = CinemaSerializers    
    permission_classes = [DjangoModelPermissionsOrAnonReadOnly]
    
    def get_queryset(self):
        queryset = Cinema.objects.all()
        return queryset


class CinemaRetriveAPIView(RetrieveAPIView): # фронтендеру поиск по ID
    serializer_class = CinemaDetailSerializer
    queryset = Cinema.objects.all()
    permission_classes = [DjangoModelPermissionsOrAnonReadOnly]


class CinemaDestroyAPIView(DestroyAPIView):
    serializer_class = CinemaDetailSerializer
    queryset = Cinema.objects.all()
    permission_classes = [DjangoModelPermissionsOrAnonReadOnly]


class CinemaUpdateAPIView(UpdateAPIView):
    serializer_class = CinemaDetailSerializer
    queryset = Cinema.objects.all()
    permission_classes = [DjangoModelPermissionsOrAnonReadOnly]
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

    permission_classes = [DjangoModelPermissionsOrAnonReadOnly]
    # def get_queryset(self):
    #     queryset = Seanses.objects.all()
    #     return queryset


class SeansesCreateAPIView(CreateAPIView): # Может создавать новые данные фронтендер через swagger
    serializer_class = SeansesSerializers    

    permission_classes = [DjangoModelPermissionsOrAnonReadOnly]
    
    def get_queryset(self):
        queryset = Seanses.objects.all()
        return queryset
    

class SeansesRetriveAPIView(RetrieveAPIView): # фронтендеру поиск по ID
    serializer_class = SeansesDetailSerializer
    queryset = Seanses.objects.all()

    permission_classes = [DjangoModelPermissionsOrAnonReadOnly]


class SeansesDestroyAPIView(DestroyAPIView):
    serializer_class = SeansesDetailSerializer
    queryset = Seanses.objects.all()

    permission_classes = [DjangoModelPermissionsOrAnonReadOnly]


class SeansesUpdateAPIView(UpdateAPIView):
    serializer_class = SeansesDetailSerializer
    queryset = Seanses.objects.all()

    permission_classes = [DjangoModelPermissionsOrAnonReadOnly]


# _________________________________________________________________________________________________
# Saloon - ListAPIView, CreateAPIView, Filter(django_filters.FilterSet), RetrieveAPIView, DestroyAPIView,

class SaloonListAPIView(ListAPIView):
    serializer_class = SaloonSerializers
    filter_backends = {filters.SearchFilter, filters.OrderingFilter, django_filters.rest_framework.DjangoFilterBackend}
    # то что нужно, фронтендер будет запрашивать и только это нужно
    permission_classes = [DjangoModelPermissionsOrAnonReadOnly]

    def get_queryset(self):

        queryset = Saloon.objects.all()
        return queryset


class SaloonCreateAPIView(CreateAPIView): # Может создавать новые данные фронтендер через swagger
    serializer_class = SaloonSerializers    
    permission_classes = [DjangoModelPermissionsOrAnonReadOnly]

    def get_queryset(self):
        queryset = Saloon.objects.all()
        return queryset


class SaloonRetriveAPIView(RetrieveAPIView): # фронтендеру поиск по ID
    serializer_class = SaloonDetailSerializer
    queryset = Saloon.objects.all()
    permission_classes = [DjangoModelPermissionsOrAnonReadOnly]


class SaloonDestroyAPIView(DestroyAPIView):
    serializer_class = SaloonDetailSerializer
    queryset = Saloon.objects.all()
    permission_classes = [DjangoModelPermissionsOrAnonReadOnly]


class SaloonUpdateAPIView(UpdateAPIView):
    serializer_class = SaloonDetailSerializer
    queryset = Saloon.objects.all()
    permission_classes = [DjangoModelPermissionsOrAnonReadOnly]

# _________________________________________________________________________________________________
# Sector - ListAPIView, CreateAPIView, Filter(django_filters.FilterSet), RetrieveAPIView, DestroyAPIView, 


class Sector_salonListAPIView(ListAPIView):
    serializer_class = Sector_salonSerializers
    filter_backends = {filters.SearchFilter, filters.OrderingFilter, django_filters.rest_framework.DjangoFilterBackend}
    permission_classes = [DjangoModelPermissionsOrAnonReadOnly]

    def get_queryset(self):
        queryset = Sector_salon.objects.all()
        return queryset


class JobtitleListAPIView(ListAPIView):
    serializer_class = JobTitleSerializers
    filter_backends = {filters.SearchFilter, filters.OrderingFilter, django_filters.rest_framework.DjangoFilterBackend}
    permission_classes = [DjangoModelPermissionsOrAnonReadOnly]

    def get_queryset(self):
        queryset = JobTitle.objects.all()
        return queryset   
    

class EmployeesListAPIView(ListAPIView):
    serializer_class = EmployeesSerializers
    filter_backends = {filters.SearchFilter, filters.OrderingFilter, django_filters.rest_framework.DjangoFilterBackend}
    filterset_fields = ('title__title',)
    search_fields = ('name', 'title', 'password', )

    permission_classes = [DjangoModelPermissionsOrAnonReadOnly]

    def get_queryset(self):
        queryset = Employees.objects.all()
        return queryset  
    

class EmployeeCreateAPIView(CreateAPIView):
    serializer_class = EmployeesSerializers
    queryset = Employees.objects.all()

    permission_classes = [DjangoModelPermissionsOrAnonReadOnly]

    def get_queryset(self):
        queryset = Employees.objects.all()
        return queryset


# ________________________________________________________________________________________________
# MovingTicket 

class MovingTicketsListCreateAPIView(ListCreateAPIView):
    serializer_class = MovingTicketsSerializer
    queryset = Moving_tickets.objects.all()
    permission_classes = [DjangoModelPermissionsOrAnonReadOnly]

    def perform_create(self, serializer):
        serializer.save(seller=self.self.request.user)

    # def create(self, request, *args, **kwargs):
    #     return super().create(request, *args, **kwargs)



class MovingTicketsRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    serializer_class = MovingTicketsSerializer
    queryset = Moving_tickets.objects.all()
    permission_classes = [DjangoModelPermissionsOrAnonReadOnly]

    def update(self, request, *args, **kwargs): # мы тут перепиали на продавца его действия 
        isinstance = self.get_object() # проверяем что пользователь является записи
        if isinstance.seller == request.user:
            return super().update(request, *args, **kwargs)
        else:
            return Response(status=status.HTTP_403_FORBIDDEN, data={'message': 'You are not the owner this record'})

# TemplateView_______________________________________________________________________________________

class CinemaTemplateView(ListView):
    template_name = 'cinema/cinema.html'
    model = Cinema

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['cinemas'] = self.model.objects.all() # sinemas - должен быть, потому что в темплейтс не будет рендериться
        return context
    

class CinemaDetailView(DetailView):
    template_name = 'cinema/cinema_detail.html'
    model = Cinema

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['cinema'] = self.model.objects.get(pk=self.kwargs['pk'])
        return context


class CinemaCreateView(CreateView):
    template_name = 'cinema/cinema_create.html'
    form_class = CinemaForm
    success_url = '/cinema_detail/'

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)
    
    # redirect to movie_detail
    def get_success_url(self):
        return reverse('cinema_detail', kwargs={'pk': self.object.pk})
    

class CinemaUpdateView(UpdateView):
    model = Cinema
    template_name = 'cinema/cinema_update.html'






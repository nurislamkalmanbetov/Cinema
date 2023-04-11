from rest_framework import serializers

from .models import  *

# Users 

class UserRegistrationSerializers(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()
    password2 = serializers.CharField()

    def validate(self, data):
        if data['password'] != data['password2']:
            raise serializers.ValidationError('Пароли не совпадают')
        return data


# Cinema_________________________________________________________________________________________________

class CinemaSerializers(serializers.ModelSerializer):
    class Meta:
        model = Cinema
        fields = ('id', 'name', 'duration', 'title', 'image', 'rental_start_date', 'rental_finish_date', 'sales_company', 'date_pub', 'author', )


class CinemaSessionSerializer(serializers.ModelSerializer):
    seanses = serializers.StringRelatedField()

    class Meta:
        model = Seanses
        fields = ['id', 'seanses', 'date', 'time']


class CinemaDetailSerializer(serializers.ModelSerializer):
    movie_seanses = CinemaSessionSerializer(many=True, read_only=True)

    class Meta:
        model = Cinema
        fields = ('id', 'name', 'duration', 'title', 'image', 'rental_start_date', 'rental_finish_date', 'sales_company', 'date_pub', 'author', 'movie_seanses')




# seanses_________________________________________________________________________________________________

class SeansesSerializers(serializers.ModelSerializer):
    seanses = serializers.StringRelatedField()
    movie = serializers.StringRelatedField()
    class Meta:
        model = Seanses
        fields = ('id', 'seanses', 'date', 'time', 'movie', )


    
class SeansesCinemaSerializer(serializers.ModelSerializer):
    # seanses = serializers.StringRelatedField()

    class Meta:
        model = Cinema
        fields = ['id', 'name', 'title', 'sales_company', ]


class SeansesDetailSerializer(serializers.ModelSerializer):
    # movie_seanses = serializers.CharField(source = 'movie.name',)

    class Meta:
        model = Seanses
        fields = ('seanses', 'date', 'time', 'movie', )


# _________________________________________________________________________________________________
# Sallon

class SaloonSerializers(serializers.ModelSerializer):
    class Meta:
        model = Saloon
        fields = ('id', 'name', 'count_place', 'description', 'number_of_rows', 'number_of_places', )

class SaloonCinemaSerializer(serializers.ModelSerializer):
    # seanses = serializers.StringRelatedField()

    class Meta:
        model = Saloon
        fields = ['id', 'name', 'count_place', 'description', 'number_of_rows', 'number_of_places', ]

class SaloonDetailSerializer(serializers.ModelSerializer):
    # movie_seanses = serializers.CharField(source = 'movie.name',)

    class Meta:
        model = Saloon
        fields = ('name', 'count_place', 'description', 'number_of_rows', 'number_of_places', )

# _________________________________________________________________________________________________


class Sector_salonSerializers(serializers.ModelSerializer):
    class Meta:
        model = Sector_salon
        fields = ('sector_salon', 'name', 'description', )


class JobTitleSerializers(serializers.ModelSerializer):
    class Meta:
        model = JobTitle
        fields = ('title', )


class EmployeesSerializers(serializers.ModelSerializer):

    title = serializers.CharField(source='title.title')  # связи между собой Foreignkey пишем это

    class Meta:
        model = Employees
        fields = ('name', 'title', 'password', )

    def create(self, validatet_data): # добавление к swagger 
        title_name = validatet_data.pop('title').get('title')
        job = JobTitle.objects.get(title=title_name)
        employee = Employees.objects.create(title=job, **validatet_data)
        return employee
    

# _________________________________________________________________________________________________
# Moving Ticket 

class MovingTicketsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Moving_tickets
        fields = ('id', 'number_ticket', 'date', 'operation', 'employee', )
        read_only_fields = ('id', 'created_at',)
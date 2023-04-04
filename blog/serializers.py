from rest_framework import serializers

from .models import  *


class CinemaSerializers(serializers.ModelSerializer):
    class Meta:
        model = Cinema
        fields = ('id', 'name', 'duration', 'title', 'image', 'rental_start_date', 'rental_finish_date', 'sales_company', 'date_pub', 'author', )


class SaloonSerializers(serializers.ModelSerializer):
    class Meta:
        model = Saloon
        fields = ('id', 'name', 'count_place', 'description', 'number_of_rows', 'number_of_places', )


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
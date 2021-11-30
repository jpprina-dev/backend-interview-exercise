from rest_framework import serializers
from django.utils.timezone import now
from .models import Pet, User


class PetsCreation(serializers.ModelSerializer):
    class Meta:
        model = Pet
        fields = ['birth_date', 'id', 'is_birth_approximate', 'name']


class PetsSerializer(serializers.ModelSerializer):
    
    age = serializers.SerializerMethodField('calculate_age')
    
    class Meta:
        model = Pet
        fields = ['id', 'name', 'age']

    def calculate_age(self, obj):
        str_response = ''
        number_of_days =  (now().date() - obj.birth_date).days
        # Calculating years
        years = number_of_days // 365
        # Calculating months
        months = (number_of_days - years * 365) // 30

        if years > 1:
            str_response = '{} years'.format(years)
        elif years == 1:
            str_response = '{} year'.format(years)
            
        if years != 0 and months !=0:
            str_response += ' and '
        
        if months > 1:
            str_response += '{} months'.format(months)
        elif months == 1:
            str_response += '{} month'.format(months)
             
        return str_response    
             

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['email', 'first_name', 'is_admin', 'last_name', 'username']
        extra_kwargs = {'password': {'required': True}}
        
        
# class Userlog(serializers.ModelSerializer):
#     class Meta:
#         model = User
#         fields = ['email', 'password']
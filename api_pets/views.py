from django.http import HttpResponse
from .models import Pet, User
from .serializers import PetsSerializer, PetsCreation, UserSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.generics import ListAPIView
from rest_framework.pagination import PageNumberPagination
import datetime

from api_pets import serializers


class PetsView(APIView):
    
    # --- POST --- endpoint: /Pets
    def post(self, request):
        serializer = PetsCreation(data=request.data)
        
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

# --- GET --- endpoint: pets/:id
class PetsListView(ListAPIView):
    serializer_class = PetsSerializer
    pagination_class = PageNumberPagination
    
    # def list(self, request):
    #     queryset = self.get_queryset()
    #     serializer = UserSerializer(queryset, many=True)
    #     return Response(serializer.data)
    
    def get_queryset(self):
        queryset = Pet.objects.all()
        pet_name = self.request.query_params.get('name')
        max_birth_date = self.request.query_params.get('max_birth_date')
        if pet_name is not None:
            queryset = queryset.filter(name__contains=pet_name)
        if max_birth_date is not None:
            queryset = queryset.filter(birth_date__lte=datetime.datetime.strptime(max_birth_date, '%Y-%m-%d'))
            
        return queryset


# --- DELETE --- endpoint: /pets
class PetsDetail(APIView):
    
    def get_pet(self, id):
        try:
            return Pet.objects.get(id=id)
    
        except Pet.DoesNotExist:
            return HttpResponse(status=status.HTTP_404_NOT_FOUND)
    
    # TODO: Comment, functinality not requested
    # def get(self, request, id):
    #     pet = self.get_pet(id)
    #     
    
    def delete(self, request, id):
        pet = self.get_pet(id)
        pet.delete()
        return Response(status=status.HTTP_200_OK)

# --- POST --- endpoint: users/login	
class UserLogin(APIView):
    
    def get_user(self, email):
        return User.objects.get(email=email)
        
    def check_password(self, input_password, user_password):
        return input_password == user_password
        
    def post(self, request):
        try:
            account = self.get_user(request.data['email'])
    
        except User.DoesNotExist:
            return HttpResponse(status=status.HTTP_404_NOT_FOUND)
        
        if not self.check_password(request.data["password"], account.password):
            return HttpResponse(status=status.HTTP_401_UNAUTHORIZED)
        
        serializer = UserSerializer(account)
        return Response(serializer.data)
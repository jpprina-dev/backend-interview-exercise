from django.urls import path
from .views import PetsView, PetsDetail, PetsListView, UserLogin

urlpatterns = [
    path('Pets/', PetsView.as_view()),
    path('pets/', PetsListView.as_view()),
    path('pets/<int:id>/', PetsDetail.as_view()),
    path('users/login/', UserLogin.as_view()),
]

from django.urls import path
from .views import CarDetailView, BuyCarView

urlpatterns = [
    path('details/<int:pk>/', CarDetailView.as_view(), name='car_detail'),
    path('buy_car/<int:pk>/', BuyCarView.as_view(), name='buy_car'),
]

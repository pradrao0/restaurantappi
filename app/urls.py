from django.urls import path
from .views import RestaurantView, MenuView, OrderView

urlpatterns = [
    path('restaurants/', RestaurantView.as_view(), name='restaurants'),
    path('menu/', MenuView.as_view(), name='menu'),
    path('orders/', OrderView.as_view(), name='orders'),
]
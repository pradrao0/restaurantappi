from rest_framework.generics import ListCreateAPIView
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from .models import Restaurant
from .serializers import RestaurantSerializer


class RestaurantView(ListCreateAPIView):
    queryset = Restaurant.objects.all()
    serializer_class = RestaurantSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


from rest_framework.generics import ListAPIView
from .models import MenuItem
from .serializers import MenuItemSerializer


class MenuView(ListAPIView):
    serializer_class = MenuItemSerializer

    def get_queryset(self):
        restaurant_id = self.request.query_params.get('restaurant_id')
        return MenuItem.objects.filter(restaurant_id=restaurant_id)
    

from rest_framework.generics import ListCreateAPIView
from rest_framework.permissions import IsAuthenticated
from .models import Order
from .serializers import OrderSerializer


class OrderView(ListCreateAPIView):
    serializer_class = OrderSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Order.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
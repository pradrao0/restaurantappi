from django_filters.rest_framework import DjangoFilterBackend

from rest_framework.generics import ListCreateAPIView, ListAPIView
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly

from .models import Restaurant, MenuItem, Order
from .serializers import RestaurantSerializer, MenuItemSerializer, OrderSerializer


# -------------------------
# RESTAURANT VIEW
# -------------------------
class RestaurantView(ListCreateAPIView):
    queryset = Restaurant.objects.all()
    serializer_class = RestaurantSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


# -------------------------
# MENU VIEW
# -------------------------
class MenuView(ListAPIView):
    serializer_class = MenuItemSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ["name"]

    def get_queryset(self):
        queryset = MenuItem.objects.all().order_by("-id")

        restaurant_id = self.request.query_params.get("restaurant_id")
        price = self.request.query_params.get("price")
        price_lte = self.request.query_params.get("price_lte")
        price_gte = self.request.query_params.get("price_gte")
        price_min = self.request.query_params.get("price_min")
        price_max = self.request.query_params.get("price_max")

        if restaurant_id:
            queryset = queryset.filter(restaurant_id=restaurant_id)

        if price:
            queryset = queryset.filter(price=price)

        if price_lte:
            queryset = queryset.filter(price__lte=price_lte)

        if price_gte:
            queryset = queryset.filter(price__gte=price_gte)

        if price_min and price_max:
            queryset = queryset.filter(price__range=(price_min, price_max))

        return queryset


# -------------------------
# ORDER VIEW
# -------------------------
class OrderView(ListCreateAPIView):
    serializer_class = OrderSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        queryset = Order.objects.filter(user=self.request.user).order_by("-id")

        status = self.request.query_params.get("status")

        if status:
            queryset = queryset.filter(status=status)

        return queryset

    def perform_create(self, serializer):
        serializer.save(
            user=self.request.user,
            status="pending"
        )
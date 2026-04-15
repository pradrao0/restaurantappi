from rest_framework import serializers
from .models import Restaurant, MenuItem, Order


# 🟢 Restaurant Serializer
class RestaurantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Restaurant
        fields = '__all__'


# 🟡 MenuItem Serializer
class MenuItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = MenuItem
        fields = '__all__'


# 🔵 Order Serializer
class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = '__all__'
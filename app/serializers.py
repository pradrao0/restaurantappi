from rest_framework import serializers
from .models import Restaurant, MenuItem, Order


# 🟢 Restaurant Serializer
class RestaurantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Restaurant
        fields = "__all__"

    def validate_name(self, value):
        value = value.strip()

        if not value:
            raise serializers.ValidationError("Restaurant name cannot be empty")

        if len(value) < 3:
            raise serializers.ValidationError("Restaurant name too short")

        return value


# 🟡 MenuItem Serializer
class MenuItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = MenuItem
        fields = "__all__"

    def validate_name(self, value):
        value = value.strip()

        if not value:
            raise serializers.ValidationError("Menu item name cannot be empty")

        return value

    def validate_price(self, value):
        if value <= 0:
            raise serializers.ValidationError("Price must be greater than 0")

        if value > 10000:
            raise serializers.ValidationError("Price is too high")

        return value


# 🔵 Order Serializer
class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = "__all__"

    def validate_quantity(self, value):
        if value <= 0:
            raise serializers.ValidationError("Quantity must be at least 1")

        if value > 50:
            raise serializers.ValidationError("Too many items in one order")

        return value
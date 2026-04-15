from django.db import models
from django.contrib.auth.models import User


# 🟢 Restaurant
class Restaurant(models.Model):
    name = models.CharField(max_length=100)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


# 🟡 Menu Item
class MenuItem(models.Model):
    name = models.CharField(max_length=100)
    price = models.IntegerField()
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


# 🔵 Order
class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    menu_item = models.ForeignKey(MenuItem, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)

    def __str__(self):
        return f"{self.user.username} ordered {self.menu_item.name}"
from django.db import models

class UserProfile(models.Model):
    name = models.CharField(max_length=100, unique=True)
    pin = models.CharField(max_length=6)

    def __str__(self):
        return self.name

class Expense(models.Model):
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    location = models.CharField(max_length=200)
    product = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.IntegerField(default=1)  # New field for quantity
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.product} - {self.price} (x{self.quantity})"
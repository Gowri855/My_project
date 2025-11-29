from django.db import models
from django.contrib.auth.models import User
from shop.models import Product   # your product model is in 'shop'

class ShippingAddress(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    address = models.CharField(max_length=255)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    zipcode = models.CharField(max_length=20)
    phone = models.CharField(max_length=15)

    def __str__(self):
        return f"{self.user.username} - {self.city}"

class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    address = models.ForeignKey(ShippingAddress, on_delete=models.SET_NULL, null=True)
    total_price = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=50, default='Pending')  # Pending / Confirmed / Delivered

    def __str__(self):
        return f"Order #{self.id}"

class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='items')
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return f"{self.product.name} x {self.quantity}"

class Payment(models.Model):
    order = models.OneToOneField(Order, on_delete=models.CASCADE, related_name='payment')
    payment_mode = models.CharField(max_length=50)
    payment_status = models.CharField(max_length=50, default='Pending')  # Pending / Completed
    payment_id = models.CharField(max_length=100, blank=True, null=True)  # gateway id

    def __str__(self):
        return f"{self.order.id} - {self.payment_mode}"

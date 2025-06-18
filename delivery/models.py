from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    ROLE_CHOICES = (
        ('student', 'Student'),
        ('admin', 'Admin'),
    )
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    role = models.CharField(max_length=10, choices=ROLE_CHOICES)

    def __str__(self):
        return f"{self.user.username} ({self.role})"


class DeliveryRequest(models.Model):
    PACKAGE_TYPES = (
        ('documents', 'Documents'),
        ('food', 'Food'),
        ('mail', 'Mail'),
    )

    STATUS_CHOICES = (
        ('pending', 'Pending'),
        ('in_transit', 'In Transit'),
        ('delivered', 'Delivered'),
    )

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    destination = models.CharField(max_length=255)
    package_type = models.CharField(max_length=20, choices=PACKAGE_TYPES)
    request_time = models.DateTimeField(auto_now_add=True)
    delivery_status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')

    def __str__(self):
        return f"Delivery #{self.id} - {self.package_type} to {self.destination}"

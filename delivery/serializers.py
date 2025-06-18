from rest_framework import serializers
from .models import DeliveryRequest

class DeliveryRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = DeliveryRequest
        fields = ['id', 'destination', 'package_type', 'delivery_status', 'request_time']
        read_only_fields = ['delivery_status', 'request_time']

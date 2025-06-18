from rest_framework import generics, permissions
from .models import DeliveryRequest
from .serializers import DeliveryRequestSerializer

# List and create deliveries for authenticated users
class DeliveryRequestListCreateAPI(generics.ListCreateAPIView):
    queryset = DeliveryRequest.objects.all()
    serializer_class = DeliveryRequestSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        # Only show deliveries belonging to the logged-in user
        return DeliveryRequest.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

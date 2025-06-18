from django.urls import path
from . import views
from . import api_views

urlpatterns = [
    # Web views
    path('', views.student_dashboard, name='student_dashboard'),
    path('create/', views.create_delivery, name='create_delivery'),
    path('register/', views.register, name='register'),

    # API endpoint
    path('api/deliveries/', api_views.DeliveryRequestListCreateAPI.as_view(), name='api_deliveries'),
]

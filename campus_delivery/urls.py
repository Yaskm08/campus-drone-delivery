from django.contrib import admin
from django.urls import path, include
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from delivery.views import RoleBasedLoginView, custom_logout

# Swagger schema configuration
schema_view = get_schema_view(
    openapi.Info(
        title="Campus Drone Delivery API",
        default_version='v1',
        description="API documentation for the Digital Flight Tracker project",
        contact=openapi.Contact(email="support@campusdelivery.com"),
    ),
    public=True,
    permission_classes=[permissions.AllowAny],
)

urlpatterns = [
    # Admin interface
    path('admin/', admin.site.urls),

    # Web views for students
    path('', include('delivery.urls')),

    # Admin dashboard views
    path('admin-panel/', include('adminpanel.urls')),

    # Custom login and logout
    path('login/', RoleBasedLoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', custom_logout, name='logout'),

    # API docs
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]

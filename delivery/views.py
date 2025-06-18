from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth import login, logout
from django.views.decorators.http import require_POST
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
from .models import DeliveryRequest, UserProfile

# Student dashboard
@login_required
def student_dashboard(request):
    deliveries = DeliveryRequest.objects.filter(user=request.user).order_by('-request_time')
    return render(request, 'student_dashboard.html', {'deliveries': deliveries})

# Create delivery request
@login_required
def create_delivery(request):
    if request.method == 'POST':
        destination = request.POST.get('destination')
        package_type = request.POST.get('package_type')
        if destination and package_type:
            DeliveryRequest.objects.create(
                user=request.user,
                destination=destination,
                package_type=package_type
            )
            return redirect('student_dashboard')
    return render(request, 'create_delivery.html')

# Register view
def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            UserProfile.objects.create(user=user, role='student')
            login(request, user)
            return redirect('student_dashboard')
    else:
        form = UserCreationForm()
    return render(request, 'register.html', {'form': form})

# Secure logout (POST only)
@require_POST
def custom_logout(request):
    logout(request)
    return redirect('login')

# Custom login view with role-based redirect
class RoleBasedLoginView(LoginView):
    def get_success_url(self):
        user = self.request.user
        if hasattr(user, 'userprofile') and user.userprofile.role == 'admin':
            return reverse_lazy('admin_dashboard')
        return reverse_lazy('student_dashboard')

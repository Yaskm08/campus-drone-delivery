from django.shortcuts import render, redirect, get_object_or_404
from delivery.models import DeliveryRequest
from django.contrib.auth.decorators import login_required, user_passes_test

# Helper function: Only allow users with role 'admin'
def is_admin(user):
    return hasattr(user, 'userprofile') and user.userprofile.role == 'admin'

@login_required
@user_passes_test(is_admin)
def admin_dashboard(request):
    deliveries = DeliveryRequest.objects.all().order_by('-request_time')

    if request.method == 'POST':
        delivery_id = request.POST.get('delivery_id')
        new_status = request.POST.get('status')

        # Optional: Validate status
        if new_status not in ['pending', 'in_transit', 'delivered']:
            return redirect('admin_dashboard')

        # Get delivery or return 404 if not found
        delivery = get_object_or_404(DeliveryRequest, id=delivery_id)
        delivery.delivery_status = new_status
        delivery.save()
        return redirect('admin_dashboard')

    return render(request, 'panel.html', {'deliveries': deliveries})

from django.shortcuts import render, redirect
from .models import Facility, HealthcareProvider, MaggotOrder


def order_start(request):

    facilities = Facility.objects.all()
    providers = HealthcareProvider.objects.all()

    if request.method == "POST":

        facility = request.POST.get("facility")
        provider = request.POST.get("provider")

        MaggotOrder.objects.create(
            facility_id=facility,
            provider_id=provider,
            wound_type=request.POST.get("wound_type"),
            wound_size=request.POST.get("wound_size"),
            urgency=request.POST.get("urgency"),
            larvae_units=request.POST.get("larvae_units"),
            application_type=request.POST.get("application_type"),
            delivery_date=request.POST.get("delivery_date"),
            notes=request.POST.get("notes"),
            contact_name=request.POST.get("contact_name"),
            phone=request.POST.get("phone"),
            email=request.POST.get("email"),
        )

        return redirect("order_success")

    return render(request, "orders/order.html", {
        "facilities": facilities,
        "providers": providers
    })


def order_success(request):
    return render(request, "orders/success.html")
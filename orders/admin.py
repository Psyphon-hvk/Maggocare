from django.contrib import admin
from .models import Facility, HealthcareProvider, MaggotOrder

# Register Facility and HealthcareProvider
admin.site.register(Facility)
admin.site.register(HealthcareProvider)

# Optional: customize MaggotOrder admin
@admin.register(MaggotOrder)
class MaggotOrderAdmin(admin.ModelAdmin):
    list_display = (
        'facility',
        'provider',
        'wound_type',
        'larvae_units',
        'urgency',
        'contact_name',
        'phone',
        'created',
    )
    list_filter = ('facility', 'provider', 'urgency')
    search_fields = ('contact_name', 'phone')
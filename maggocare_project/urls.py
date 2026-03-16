from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),

    # homepage and main pages
    path('', include('core.urls')),

    # order system
    path('orders/', include('orders.urls')),
]
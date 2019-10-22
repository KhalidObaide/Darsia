from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    # darsia.com/ar/
    path('ar/', include('ar.urls')),

    # darsia.com/admin
    path('admin/', admin.site.urls),
]

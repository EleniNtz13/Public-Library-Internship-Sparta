from django.contrib import admin  # Import Django's admin module
from django.urls import path, include  # Import functions to define URL patterns and include app URLs

urlpatterns = [  # List of URL patterns for the project
    path('admin/', admin.site.urls),  # Route for the Django admin interface
    path('', include('main.urls')),  # Include URLs from the "main" app at the root path
]

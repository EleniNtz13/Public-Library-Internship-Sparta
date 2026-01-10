from django.contrib import admin  # Import Django admin module
from django.urls import path, include  # Import path and include for URL routing
from django.views.generic.base import TemplateView  # Import generic template view


urlpatterns = [
    path("admin/", admin.site.urls),  
    # URL for Django admin interface

    path("accounts/", include("django.contrib.auth.urls")),  
    # Include default Django authentication URLs (login, logout, password management)

    path('', include('main.urls')),  
    # Include all URLs defined in the 'main' app

    path('', TemplateView.as_view(template_name='home.html'), name='home'),  
    # Serve home.html at the root URL as a TemplateView
]

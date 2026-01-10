from django.contrib import admin  # Import Django's admin module
from django.urls import path, include  # Import functions to define URL patterns and include other URL configs
from . import views  # Import views from the current app
from .views import upload_excel, show_people, SignUpView, autocomplete_title, autocomplete_ekdoths  # Import specific view functions/classes

urlpatterns = [  # List of URL patterns for this app
    path('', views.home, name='home'),  # Home page
    path('signup/', SignUpView.as_view(), name='signup'),  # Sign-up page using a class-based view
    path('accounts/', include('django.contrib.auth.urls')),  # Include built-in authentication URLs (login, logout, password reset, etc.)
    path('people/', views.show_people, name='show_people'),  # Display list of people
    path('upload/', views.upload_excel, name='upload_excel'),  # Upload Excel file
    path('duplicates/', views.resolve_duplicates, name='resolve_duplicates'),  # Resolve duplicates page
    path('duplicates/handle/', views.handle_duplicate, name='handle_duplicate'),  # Handle individual duplicate
    path('person/edit/<str:pk>/', views.edit_person, name='edit_person'),  # Edit a person by primary key
    path('skip-all-duplicates/', views.skip_all_duplicates, name='skip_all_duplicates'),  # Skip all duplicates action
    path('add-person/', views.add_person, name='add_person'),  # Add a new person manually
    path('ajax/autocomplete/title/', views.autocomplete_title, name='autocomplete_title'),  # AJAX endpoint for title autocomplete
    path('ajax/autocomplete/ekdoths/', views.autocomplete_ekdoths, name='autocomplete_ekdoths'),  # AJAX endpoint for publisher autocomplete
]

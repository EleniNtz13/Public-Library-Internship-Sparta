from django.contrib import admin
from django.urls import path, include
from . import views
from .views import upload_excel, show_people, SignUpView, autocomplete_title, autocomplete_ekdoths



urlpatterns = [
    path('', views.home, name='home'),
    path('signup/', SignUpView.as_view(), name='signup'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('people/', views.show_people, name='show_people'),
    path('upload/', views.upload_excel, name='upload_excel'),
    path('duplicates/', views.resolve_duplicates, name='resolve_duplicates'),
    path('duplicates/handle/', views.handle_duplicate, name='handle_duplicate'),
    path('person/edit/<str:pk>/', views.edit_person, name='edit_person'),
    path('skip-all-duplicates/', views.skip_all_duplicates, name='skip_all_duplicates'),
    path('add-person/', views.add_person, name='add_person'),
    path('ajax/autocomplete/title/', views.autocomplete_title, name='autocomplete_title'),
    path('ajax/autocomplete/ekdoths/', views.autocomplete_ekdoths, name='autocomplete_ekdoths'),

    

]

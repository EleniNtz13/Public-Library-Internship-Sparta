from django.urls import path
from . import views

urlpatterns = [
    path('', views.show_books, name='show_books'),    # root του app
    path('add/', views.add_book, name='add_book'),
    path('upload-excel/', views.upload_excel, name='upload_excel')
]

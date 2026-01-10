from django.contrib import admin  # Import Django's admin module
from .models import UploadLog  # Import the UploadLog model from the current app

@admin.register(UploadLog)  # Register the UploadLog model with the admin site
class UploadLogAdmin(admin.ModelAdmin):  # Define a custom admin interface for UploadLog
    list_display = ("filename", "user", "uploaded_at", "rows_added", "rows_updated")  # Columns to display in the admin list view
    list_filter = ("user", "uploaded_at")  # Enable filtering by user and upload date

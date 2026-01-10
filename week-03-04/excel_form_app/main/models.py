from django.db import models  # Import Django's models module for database models
from django.contrib.auth.models import User  # Import the User model for authentication

class Person(models.Model):  # Define the Person model
    ari8mosEisagoghs = models.CharField(unique=True, primary_key=True, max_length=200, blank=True)  # Primary key, unique entry number
    hmeromhnia_eis = models.CharField(max_length=200, null=True, blank=True)  # Entry date
    syggrafeas = models.CharField(max_length=200, null=True, blank=True)  # Author name
    koha = models.CharField(max_length=200, null=True, blank=True)  # KOHA code or identifier
    titlos = models.CharField(max_length=200, null=True, blank=True)  # Title of the book/item
    ekdoths = models.CharField(max_length=200, null=True, blank=True)  # Publisher
    ekdosh = models.CharField(max_length=200, null=True, blank=True)  # Edition
    etosEkdoshs = models.CharField(max_length=20, null=True, blank=True)  # Year of publication
    toposEkdoshs = models.CharField(max_length=200, null=True, blank=True)  # Place of publication
    sxhma = models.CharField(max_length=200, null=True, blank=True)  # Format or schema
    selides = models.CharField(max_length=50, null=True, blank=True)  # Number of pages
    tomos = models.CharField(max_length=50, null=True, blank=True)  # Volume number
    troposPromPar = models.CharField(max_length=200, null=True, blank=True)  # Method of acquisition
    ISBN = models.CharField(max_length=50, null=True, blank=True)  # ISBN number
    sthlh1 = models.CharField(max_length=200, null=True, blank=True)  # Extra column 1
    sthlh2 = models.CharField(max_length=200, null=True, blank=True)  # Extra column 2

    def __str__(self):  # String representation of the Person model
        return self.ari8mosEisagoghs  # Return the entry number

class UploadLog(models.Model):  # Define a model to log uploads
    user = models.ForeignKey(  # Link to the User who performed the upload
        User,  # Reference User model
        on_delete=models.CASCADE,  # Delete logs if the user is deleted
        related_name="uploads"  # Allow reverse lookup via user.uploads
    )
    uploaded_at = models.DateTimeField(auto_now_add=True)  # Timestamp of upload
    filename = models.CharField(max_length=255)  # Name of the uploaded file
    rows_added = models.PositiveIntegerField(default=0)  # Count of rows added
    rows_updated = models.PositiveIntegerField(default=0)  # Count of rows updated

    def __str__(self):  # String representation of the UploadLog model
        return f"{self.filename} by {self.user.username} on {self.uploaded_at}"  # Return descriptive log info

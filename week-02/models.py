from django.db import models  # Import Django's models module for defining database models
from django.contrib.auth.models import User  # Import the built-in User model for authentication

class Person(models.Model):  # Define a database model named Person
    ari8mosEisagoghs = models.CharField(unique=True, primary_key=True, max_length=200, blank=True)  # Unique primary key field for entry number
    hmeromhnia_eis = models.CharField(max_length=200, null=True, blank=True)  # Field to store entry date
    syggrafeas = models.CharField(max_length=200, null=True, blank=True)  # Field to store author name
    koha = models.CharField(max_length=200, null=True, blank=True)  # Field to store KOHA identifier or code
    titlos = models.CharField(max_length=200, null=True, blank=True)  # Field to store title
    ekdoths = models.CharField(max_length=200, null=True, blank=True)  # Field to store publisher
    ekdosh = models.CharField(max_length=200, null=True, blank=True)  # Field to store edition
    etosEkdoshs = models.CharField(max_length=20, null=True, blank=True)  # Field to store year of publication
    toposEkdoshs = models.CharField(max_length=200, null=True, blank=True)  # Field to store place of publication
    sxhma = models.CharField(max_length=200, null=True, blank=True)  # Field to store format or schema
    selides = models.CharField(max_length=50, null=True, blank=True)  # Field to store number of pages
    tomos = models.CharField(max_length=50, null=True, blank=True)  # Field to store volume information
    troposPromPar = models.CharField(max_length=200, null=True, blank=True)  # Field to store acquisition method
    ISBN = models.CharField(max_length=50, null=True, blank=True)  # Field to store ISBN number
    sthlh1 = models.CharField(max_length=200, null=True, blank=True)  # Custom column 1 for extra data
    sthlh2 = models.CharField(max_length=200, null=True, blank=True)  # Custom column 2 for extra data

    def __str__(self):  # Define string representation of the Person object
        return self.name  # Return the name attribute when object is printed

class UploadLog(models.Model):  # Define a database model to log upload actions
    user = models.ForeignKey(  # Define a foreign key relationship to the User model
        User,  # Reference the User model
        on_delete=models.CASCADE,  # Delete upload logs if the related user is deleted
        related_name="uploads"  # Allow reverse access via user.uploads
    )
    uploaded_at = models.DateTimeField(auto_now_add=True)  # Store the timestamp when the upload occurred
    filename = models.CharField(max_length=255)  # Store the name of the uploaded file
    rows_added = models.PositiveIntegerField(default=0)  # Store the number of rows added during upload
    rows_updated = models.PositiveIntegerField(default=0)  # Store the number of rows updated during upload

    def __str__(self):  # Define string representation of the UploadLog object
        return f"{self.filename} by {self.user.username} on {self.uploaded_at}"  # Return a descriptive string for the log entry

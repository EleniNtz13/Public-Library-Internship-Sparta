from django import forms  # Import Django forms module
from .models import Person  # Import the Person model from the current app
from django.contrib.auth.forms import UserCreationForm  # Import Django's built-in user creation form
from django.contrib.auth.models import User  # Import the User model for authentication

class PersonForm(forms.ModelForm):  # Define a ModelForm for the Person model
    class Meta:  # Metadata for the form
        model = Person  # Set the model to Person
        fields = [  # List all fields to include in the form
            'ari8mosEisagoghs',
            'hmeromhnia_eis',
            'syggrafeas',
            'koha',
            'titlos',
            'ekdoths',
            'ekdosh',
            'etosEkdoshs',
            'toposEkdoshs',
            'sxhma',
            'selides',
            'tomos',
            'troposPromPar',
            'ISBN',
            'sthlh1',
            'sthlh2',
        ]

class CustomUserCreationForm(UserCreationForm):  # Define a custom user registration form
    email = forms.EmailField(  # Add an email field
        required=True,  # Make email required
        help_text="Required. Enter a valid email address."  # Provide help text for the field
    )

    class Meta:  # Metadata for the form
        model = User  # Set the model to User
        fields = ("username", "email", "password1", "password2")  # Fields to include in the form

    def clean_email(self):  # Custom validation for email field
        email = self.cleaned_data.get("email")  # Get the cleaned email value
        if User.objects.filter(email=email).exists():  # Check if email is already registered
            raise forms.ValidationError("This email is already registered.")  # Raise validation error if duplicate
        return email  # Return validated email

class UploadExcelForm(forms.Form):  # Define a standard form for Excel file upload
    excel_file = forms.FileField(label="")  # Single file input with no label text

class PersonManualForm(forms.ModelForm):  # Another ModelForm for manual Person entry
    class Meta:  # Metadata for the form
        model = Person  # Set the model to Person
        exclude = ['ari8mosEisagoghs']  # Exclude the primary key field from the form
        widgets = {  # Customize widgets for certain fields
            'titlos': forms.Textarea(attrs={'rows': 1}),  # Single-row textarea for title
            'syggrafeas': forms.Textarea(attrs={'rows': 1}),  # Single-row textarea for author
            'troposPromPar': forms.Textarea(attrs={'rows': 1}),  # Single-row textarea for acquisition method
            'ekdoths': forms.Textarea(attrs={'rows': 1}),  # Single-row textarea for publisher
            'koha': forms.Textarea(attrs={'rows': 1}),  # Single-row textarea for KOHA code
        }

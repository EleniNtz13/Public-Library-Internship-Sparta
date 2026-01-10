"""
WSGI config for excel_form_app project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/6.0/howto/deployment/wsgi/
"""

import os  # Import the os module to interact with environment variables

from django.core.wsgi import get_wsgi_application  # Import function to get WSGI application callable

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'excel_form_app.settings')  # Set default settings module for Django

application = get_wsgi_application()  # Create WSGI application callable used by WSGI servers



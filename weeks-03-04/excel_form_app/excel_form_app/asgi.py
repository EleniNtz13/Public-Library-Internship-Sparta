"""
ASGI config for excel_form_app project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/6.0/howto/deployment/asgi/
"""

import os  # Import the os module to interact with environment variables

from django.core.asgi import get_asgi_application  # Import Django's function to get the ASGI application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'excel_form_app.settings')  # Set the default Django settings module if not already defined

application = get_asgi_application()  # Create the ASGI application callable used by the server
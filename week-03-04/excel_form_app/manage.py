#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""  # Module docstring

import os  # OS module for environment settings
import sys  # Sys module for command-line arguments


def main():
    """Run administrative tasks."""  # Main function docstring
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'excel_form_app.settings')  
    # Set default Django settings module if not set in environment

    try:
        from django.core.management import execute_from_command_line  # Import Django CLI
    except ImportError as exc:  
        # Handle ImportError if Django is not installed
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc  # Raise original exception for context

    execute_from_command_line(sys.argv)  
    # Execute command-line arguments using Django's management utility


if __name__ == '__main__':
    main()  # Call main function if script is run directly

"""Application configuration for the greeting app.

This module defines the GreetingConfig class which configures
the greeting application with its default settings.
"""
from django.apps import AppConfig


class GreetingConfig(AppConfig):
    """Configuration class for the greeting application.

    Attributes:
        default_auto_field (str):
            The default field type for automatic primary keys
        name (str): The name of this application (must match the package name)
    """

    default_auto_field = 'django.db.models.BigAutoField'
    name = 'greeting'

    def ready(self):
        """Run initialization code when Django starts.

        This method can be used to register signals or perform other
        one-time initialization tasks.
        """
# Import and register signals here if needed

        pass
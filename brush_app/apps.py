from django.apps import AppConfig


class BrushAppConfig(AppConfig):
    """
    Configuration class for the Brush app.

    Attributes:
        default_auto_field (str):
        The default auto field for model primary keys.
        name (str): The name of the app (used in settings and other places).
    """
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'brush_app'

from django.apps import AppConfig


class CssprintsConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = 'cssprints'

    def ready(self):
        import cssprints

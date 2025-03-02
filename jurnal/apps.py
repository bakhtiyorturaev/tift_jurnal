from django.apps import AppConfig


class JurnalConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'jurnal'

    def ready(self):
        import jurnal.signals
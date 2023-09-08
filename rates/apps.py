from django.apps import AppConfig


class RatesConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'rates'

    def ready(self):
        from .rates_scheduler import rates_updater
        rates_updater.start()


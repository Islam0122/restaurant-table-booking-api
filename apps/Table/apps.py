from django.apps import AppConfig


class TableConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'apps.Table'
    verbose_name = 'Столики в ресторане'

    def ready(self):
        import apps.Table.signals

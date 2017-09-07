from django.apps import AppConfig


class MyadminConfig(AppConfig):
    name = 'myadmin'
    def ready(self):
        super().ready()
        from django.utils.module_loading import autodiscover_modules
        autodiscover_modules('myadmin')

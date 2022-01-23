from django.apps import AppConfig
from django.db.models.signals import post_delete

class BlogsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'blogs'

    def ready(self):
        from . import signals
        # Explicitly connect a signal handler.
        post_delete.connect(signals.remove_post_read_marks)

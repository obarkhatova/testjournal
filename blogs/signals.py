from django.db.models.signals import post_delete
from django.dispatch import receiver


@receiver(post_delete)
def remove_post_read_marks(sender, **kwargs):
    pass
from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Magazine, Statistics

@receiver(post_save, sender=Magazine)
def create_or_update_statistics(sender, instance, created, **kwargs):
    if created:
        Statistics.objects.create(magazine=instance)
    else:
        stats = instance.statistics
        if stats:
            stats.save()

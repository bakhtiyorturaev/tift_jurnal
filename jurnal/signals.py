from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Magazine, Statistics, AboutMagazine


@receiver(post_save, sender=Magazine)
def create_or_update_statistics(sender, instance, created, **kwargs):
    if created:
        Statistics.objects.create(magazine=instance)
    else:
        stats = instance.statistics
        if stats:
            stats.save()


@receiver(post_save, sender=Magazine)
def update_about_magazine(sender, instance, **kwargs):
    AboutMagazine.objects.filter(magazine=instance).update(
        magazine_name_uz=instance.name_uz,
        magazine_name_ru=instance.name_ru,
        magazine_name_en=instance.name_en
    )
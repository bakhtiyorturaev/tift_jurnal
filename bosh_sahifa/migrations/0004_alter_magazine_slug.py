# Generated by Django 5.1.6 on 2025-02-27 17:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bosh_sahifa', '0003_alter_magazine_which_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='magazine',
            name='slug',
            field=models.SlugField(help_text='Namuna: 1-son-01-2025-yil', unique=True, verbose_name='Slug'),
        ),
    ]

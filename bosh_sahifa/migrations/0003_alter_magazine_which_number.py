# Generated by Django 5.1.6 on 2025-02-21 20:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bosh_sahifa', '0002_remove_article_upload_file_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='magazine',
            name='which_number',
            field=models.CharField(help_text='Namuna: 1-son | 01.2025', max_length=50, verbose_name='Jurnal soni'),
        ),
    ]

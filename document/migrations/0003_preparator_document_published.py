# Generated by Django 3.1 on 2020-08-08 16:09

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('document', '0002_preparator_document'),
    ]

    operations = [
        migrations.AddField(
            model_name='preparator_document',
            name='published',
            field=models.DateField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
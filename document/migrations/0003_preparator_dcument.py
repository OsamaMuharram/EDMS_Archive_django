# Generated by Django 3.0.7 on 2020-08-08 01:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cabinet', '0002_auto_20200808_0055'),
        ('document', '0002_auto_20200808_0055'),
    ]

    operations = [
        migrations.CreateModel(
            name='preparator_dcument',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150)),
                ('description', models.CharField(max_length=500)),
                ('boss_name', models.CharField(max_length=150)),
                ('create_date', models.DateField(auto_now=True)),
                ('management_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cabinet.cabinet')),
            ],
        ),
    ]

# Generated by Django 3.1 on 2020-08-09 04:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='employee',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('employee_name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='cabinet',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Management_name', models.CharField(max_length=30)),
                ('description', models.CharField(max_length=200)),
                ('Mgment_path', models.CharField(blank=True, max_length=200, null=True)),
                ('branuch_from', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='cabinet.cabinet')),
                ('employee', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cabinet.employee')),
            ],
        ),
    ]

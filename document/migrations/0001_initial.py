# Generated by Django 3.0.7 on 2020-08-05 22:48

from django.db import migrations, models
import django.db.models.deletion
import document.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('cabinet', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='document',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('file_uploded', models.FileField(upload_to=document.models.Management_path)),
                ('employee_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cabinet.employee')),
                ('select_cabinet', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cabinet.cabinet')),
            ],
        ),
    ]

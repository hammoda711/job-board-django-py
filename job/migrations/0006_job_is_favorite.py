# Generated by Django 5.0.7 on 2024-07-25 01:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('job', '0005_alter_job_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='job',
            name='is_favorite',
            field=models.BooleanField(default=False),
        ),
    ]

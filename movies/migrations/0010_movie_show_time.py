# Generated by Django 5.1.5 on 2025-02-13 17:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0009_alter_theater_total_seats'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='show_time',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]

# Generated by Django 5.1.5 on 2025-02-13 17:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0007_booking_amount'),
    ]

    operations = [
        migrations.AddField(
            model_name='theater',
            name='total_seats',
            field=models.PositiveIntegerField(default=100),
        ),
    ]

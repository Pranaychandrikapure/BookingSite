# Generated by Django 5.1.5 on 2025-02-10 18:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0004_rename_show_time_booking_date_remove_booking_price_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='booking',
            name='price',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=10),
        ),
    ]

# Generated by Django 4.1 on 2022-08-29 09:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0004_flightimage_remove_flight_destination_picture'),
    ]

    operations = [
        migrations.AddField(
            model_name='flightimage',
            name='flight',
            field=models.OneToOneField(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='base.flight'),
        ),
    ]
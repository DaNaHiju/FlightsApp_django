# Generated by Django 4.1 on 2022-08-28 15:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='address',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='credit_card_no',
            field=models.CharField(blank=True, max_length=20, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='phone_no',
            field=models.CharField(blank=True, max_length=20, null=True, unique=True),
        ),
    ]

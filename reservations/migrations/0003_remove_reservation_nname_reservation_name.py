# Generated by Django 5.1.3 on 2024-12-07 00:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("reservations", "0002_remove_reservation_name_reservation_nname"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="reservation",
            name="nname",
        ),
        migrations.AddField(
            model_name="reservation",
            name="name",
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]

# Generated by Django 5.1.3 on 2024-12-07 00:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("reservations", "0003_remove_reservation_nname_reservation_name"),
    ]

    operations = [
        migrations.RenameField(
            model_name="reservation",
            old_name="date",
            new_name="start_date",
        ),
        migrations.RenameField(
            model_name="reservation",
            old_name="time",
            new_name="start_time",
        ),
    ]
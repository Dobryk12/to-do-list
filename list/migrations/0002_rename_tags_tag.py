# Generated by Django 5.0.3 on 2024-03-11 09:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("list", "0001_initial"),
    ]

    operations = [
        migrations.RenameModel(
            old_name="Tags",
            new_name="Tag",
        ),
    ]

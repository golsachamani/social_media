# Generated by Django 4.2.16 on 2024-10-21 18:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("account", "0005_profile_is_private"),
    ]

    operations = [
        migrations.AlterField(
            model_name="profile",
            name="is_private",
            field=models.BooleanField(default=False),
        ),
    ]
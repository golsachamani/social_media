# Generated by Django 4.2.16 on 2024-10-19 19:55

from django.db import migrations
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ("blog", "0006_post_replied_to_alter_post_image"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="post",
            name="image",
        ),
        migrations.AlterField(
            model_name="post",
            name="content",
            field=tinymce.models.HTMLField(),
        ),
    ]

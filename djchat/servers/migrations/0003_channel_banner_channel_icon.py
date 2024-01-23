# Generated by Django 5.0 on 2024-01-15 18:40

import servers.models
import servers.validators
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("servers", "0002_category_icon_alter_channel_owner_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="channel",
            name="banner",
            field=models.ImageField(
                blank=True,
                null=True,
                upload_to=servers.models.channel_banner_file_path,
                validators=[servers.validators.validate_image_extension],
                verbose_name="Banner",
            ),
        ),
        migrations.AddField(
            model_name="channel",
            name="icon",
            field=models.ImageField(
                blank=True,
                null=True,
                upload_to=servers.models.channel_icon_file_path,
                validators=[
                    servers.validators.validate_icon_image_size,
                    servers.validators.validate_image_extension,
                ],
                verbose_name="Icon",
            ),
        ),
    ]

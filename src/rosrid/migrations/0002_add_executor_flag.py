# Generated by Django 4.1.4 on 2023-05-18 19:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("rosrid", "0001_init_rosrid_tables"),
    ]

    operations = [
        migrations.AddField(
            model_name="active",
            name="is_executor",
            field=models.BooleanField(
                default=False,
                help_text="Признак того, можем ли мы записать в актив университету",
            ),
        ),
    ]

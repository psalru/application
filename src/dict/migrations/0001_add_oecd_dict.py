# Generated by Django 4.1.4 on 2023-05-13 19:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="OECDGroup",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True, null=True)),
                ("deleted_at", models.DateTimeField(blank=True, null=True)),
                ("code", models.IntegerField(help_text="Год группы", unique=True)),
                (
                    "title",
                    models.CharField(
                        help_text="Название группы", max_length=255, unique=True
                    ),
                ),
                (
                    "title_src",
                    models.CharField(
                        help_text="Название группы из источника (английский)",
                        max_length=255,
                        unique=True,
                    ),
                ),
            ],
            options={
                "verbose_name_plural": "OECD groups",
                "db_table": "dict_oecd_group",
            },
        ),
        migrations.CreateModel(
            name="OECD",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True, null=True)),
                ("deleted_at", models.DateTimeField(blank=True, null=True)),
                (
                    "code",
                    models.CharField(help_text="Год группы", max_length=5, unique=True),
                ),
                (
                    "title",
                    models.CharField(help_text="Название", max_length=255, unique=True),
                ),
                (
                    "title_src",
                    models.CharField(
                        help_text="Название из источника (английский)",
                        max_length=255,
                        unique=True,
                    ),
                ),
                (
                    "oecd_group",
                    models.ForeignKey(
                        help_text="Ссылка на OECD группу",
                        on_delete=django.db.models.deletion.PROTECT,
                        to="dict.oecdgroup",
                    ),
                ),
            ],
            options={
                "verbose_name_plural": "OECD",
                "db_table": "dict_oecd",
            },
        ),
    ]
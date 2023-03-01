# Generated by Django 4.1.4 on 2023-03-01 20:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("geo", "0001_init_geo_tables"),
    ]

    operations = [
        migrations.CreateModel(
            name="Status",
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
                    "title",
                    models.CharField(
                        help_text="Название статуса организации", max_length=255
                    ),
                ),
            ],
            options={
                "verbose_name_plural": "Statuses",
            },
        ),
        migrations.CreateModel(
            name="University",
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
                    "title",
                    models.CharField(
                        help_text="Полное официальное название",
                        max_length=255,
                        unique=True,
                    ),
                ),
                (
                    "title_short",
                    models.CharField(
                        help_text="Краткое официальное название",
                        max_length=255,
                        unique=True,
                    ),
                ),
                (
                    "title_display",
                    models.CharField(
                        help_text="Отображаемое краткое название",
                        max_length=255,
                        unique=True,
                    ),
                ),
                (
                    "geo_point",
                    models.CharField(
                        help_text="Геоточка нахождения организации", max_length=50
                    ),
                ),
                (
                    "domain",
                    models.CharField(
                        help_text="Основной домен (сайт) организации",
                        max_length=255,
                        unique=True,
                    ),
                ),
                (
                    "mon_id",
                    models.IntegerField(
                        blank=True,
                        help_text="ID университета в «1-Мониторинг»",
                        null=True,
                    ),
                ),
                (
                    "city",
                    models.ForeignKey(
                        help_text="Город (фактическое нахождение)",
                        on_delete=django.db.models.deletion.PROTECT,
                        to="geo.city",
                    ),
                ),
            ],
            options={
                "verbose_name_plural": "Universities",
            },
        ),
        migrations.CreateModel(
            name="UniversityStatus",
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
                ("start", models.DateField(help_text="Дата начала действия статуса")),
                (
                    "end",
                    models.DateField(
                        blank=True,
                        help_text="Дата окончания действия статуса",
                        null=True,
                    ),
                ),
                (
                    "status",
                    models.ForeignKey(
                        help_text="Ссылка на статус",
                        on_delete=django.db.models.deletion.PROTECT,
                        to="university.status",
                    ),
                ),
                (
                    "university",
                    models.ForeignKey(
                        help_text="Ссылка на организацию",
                        on_delete=django.db.models.deletion.CASCADE,
                        to="university.university",
                    ),
                ),
            ],
            options={
                "verbose_name_plural": "University statuses",
                "db_table": "university_university_status",
            },
        ),
    ]

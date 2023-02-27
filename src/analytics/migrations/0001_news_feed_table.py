# Generated by Django 4.1.4 on 2022-12-24 14:09

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="NewsFeed",
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
                ("deleted_at", models.DateTimeField(null=True)),
                (
                    "hash",
                    models.TextField(
                        help_text="Хэш из ключевого слова и ссылка для уникализации",
                        unique=True,
                    ),
                ),
                ("topic", models.TextField(help_text="Основная тема")),
                (
                    "keyword",
                    models.TextField(
                        help_text="Ключевое слово по которому ищет Google Alerts"
                    ),
                ),
                ("date", models.DateField(help_text="Дата публикации")),
                ("domain", models.TextField(help_text="Домен источника", null=True)),
                ("url", models.TextField(help_text="Ссылка на первоисточник")),
                ("title", models.TextField(help_text="Заголовок")),
                ("content", models.TextField(help_text="Содержание", null=True)),
                ("s3_bucket", models.TextField(help_text="Баккет в S3")),
                (
                    "s3_key",
                    models.TextField(help_text="Путь к HTML-контенту в S3", null=True),
                ),
            ],
            options={
                "abstract": False,
            },
        ),
    ]
from django.db import models


class BaseModels(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(null=True)

    class Meta:
        abstract = True


class NewsFeed(BaseModels):
    keyword = models.TextField(help_text='Ключевое слово по которому ищет Google Alerts')
    date = models.DateField(help_text='Дата публикации')
    domain = models.TextField(help_text='Домен источника')
    url = models.TextField(unique=True, help_text='Ссылка на первоисточник')
    title = models.TextField(help_text='Заголовок')
    content = models.TextField(help_text='Содержание')
    s3_bucket = models.TextField(help_text='Баккет в S3')
    s3_key = models.TextField(help_text='Путь к HTML-контенту в S3')

    def __str__(self) -> str:
        return self.title

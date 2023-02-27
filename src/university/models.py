from django.db import models
from config.models import BaseModel
from geo.models import City


class University(BaseModel):
    title = models.CharField(max_length=255, unique=True, help_text='Полное официальное название')
    title_short = models.CharField(max_length=255, unique=True, help_text='Краткое официальное название')
    title_display = models.CharField(max_length=255, unique=True, help_text='Отображаемое краткое название')
    city = models.ForeignKey(City, on_delete=models.PROTECT, help_text='Город (фактическое нахождение)')
    geo_point = models.CharField(max_length=50, help_text='Геоточка нахождения организации')
    domain = models.CharField(max_length=255, unique=True, help_text='Основной домен (сайт) организации')
    mon_id = models.IntegerField(unique=True, help_text='ID университета в «1-Мониторинг»')

    def __str__(self):
        return self.title_short

    class Meta:
        verbose_name_plural = 'Universities'


class Status(BaseModel):
    title = models.CharField(max_length=255, help_text='Название статуса организации')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = 'Statuses'


class UniversityStatus(BaseModel):
    start = models.DateField(help_text='Дата начала действия статуса')
    end = models.DateField(null=True, blank=True, help_text='Дата окончания действия статуса')
    university = models.ForeignKey(University, on_delete=models.CASCADE, help_text='Ссылка на организацию')
    status = models.ForeignKey(Status, on_delete=models.PROTECT, help_text='Ссылка на статус')

    def __str__(self):
        return f'{self.status} {self.start} - {self.end}: {self.university}'

    class Meta:
        db_table = 'university_university_status'
        verbose_name_plural = 'University statuses'

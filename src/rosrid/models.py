from django.db import models
from config.models import BaseModel
from university.models import University
from dict.models import OECD


class RosridUniversity(BaseModel):
    university = models.ForeignKey(University, related_name='rosrid', on_delete=models.PROTECT, help_text='Ссылка на университет')
    rosrid_id = models.CharField(unique=True, max_length=25, help_text='ID организации в ЕГИСУ НИОКТР')

    def __str__(self):
        return self.university.title

    class Meta:
        db_table = 'rosrid_rosrid_university'
        verbose_name_plural = 'RosRID universities'


class ActiveType(BaseModel):
    title = models.CharField(max_length=255, help_text='Название типа актива')
    title_short = models.CharField(max_length=255, help_text='Краткое название типа актива')

    def __str__(self):
        return self.title

    class Meta:
        db_table = 'rosrid_active_type'


class Active(BaseModel):
    rosrid_university = models.ForeignKey(RosridUniversity, on_delete=models.PROTECT, help_text='Ссылка на университет в ЕГИСУ НИОКТР')
    object_id = models.CharField(max_length=25, help_text='Уникальный ID актива внутри ЕГИСУ НИОКТР')
    type = models.ForeignKey(ActiveType, on_delete=models.PROTECT, help_text='Ссылка на тип актива')
    date = models.DateField(help_text='Дата из ЕГИСУ НИОКТР')
    title = models.CharField(max_length=2048, help_text='Название актива')
    oecd = models.ManyToManyField(OECD, help_text='Связи с OECD')
    url = models.CharField(max_length=255, help_text='Ссылка на актив в ЕГИСУ НИОКТР')
    is_executor = models.BooleanField(default=False, help_text='Признак того, можем ли мы считать актив за университетом')
    s3_bucket = models.CharField(max_length=255, help_text='Баккет в S3')
    s3_key = models.CharField(max_length=255, help_text='Ссылка на JSON содержащий подробные данные актива')

    def __str__(self):
        return f"{self.type.title}: «{self.title}»"

from django.db import models
from config.models import BaseModel


class OECDGroup(BaseModel):
    code = models.IntegerField(unique=True, help_text='Год группы')
    title = models.CharField(max_length=255, unique=True, help_text='Название группы')
    title_src = models.CharField(max_length=255, unique=True, help_text='Название группы из источника (английский)')

    def __str__(self):
        return f"{self.code} - {self.title}"

    class Meta:
        db_table = 'dict_oecd_group'
        verbose_name_plural = 'OECD groups'


class OECD(BaseModel):
    code = models.CharField(max_length=5, unique=True, help_text='Год группы')
    title = models.CharField(max_length=255, unique=True, help_text='Название')
    title_src = models.CharField(max_length=255, unique=True, help_text='Название из источника (английский)')
    oecd_group = models.ForeignKey(OECDGroup, on_delete=models.PROTECT, help_text='Ссылка на OECD группу')

    def __str__(self):
        return f"{self.code} - {self.title}"

    class Meta:
        db_table = 'dict_oecd'
        verbose_name_plural = 'OECD'

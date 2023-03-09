from django.db import models
from config.models import BaseModel


class FederalDistrict(BaseModel):
    title = models.CharField(max_length=255, help_text='Название федерального округа')
    title_short = models.CharField(max_length=255, help_text='Краткое название федерального округа')
    capital = models.ForeignKey('City', null=True, help_text='Столица федерального округа', on_delete=models.PROTECT)
    square = models.FloatField(help_text='Площадь федерального округа')

    def __str__(self):
        return self.title_short

    class Meta:
        db_table = 'geo_federal_district'


class FederalRegion(BaseModel):
    class FederalRegionType(models.TextChoices):
        REPUBLIC = 'republic', 'Республика'
        EDGE = 'edge', 'Край'
        AREA = 'area', 'Область'
        CITY = 'city', 'Город федерального значения'
        REGION = 'region', 'Регион'
        OKRUG = 'okrug', 'Автономный округ'

    title = models.CharField(max_length=255, help_text='Название региона')
    type = models.CharField(max_length=27, choices=FederalRegionType.choices, help_text='Тип региона')
    capital = models.ForeignKey('City', null=True, help_text='Столица региона', on_delete=models.PROTECT)
    square = models.FloatField(help_text='Площадь региона')
    okato = models.IntegerField(help_text='ОКАТО')

    def __str__(self):
        return self.title

    class Meta:
        db_table = 'geo_federal_region'


class City(BaseModel):
    title = models.CharField(max_length=255, help_text='Название города')
    federal_district = models.ForeignKey(FederalDistrict, help_text='Федеральный округ', on_delete=models.PROTECT)
    federal_region = models.ForeignKey(FederalRegion, help_text='Регион', on_delete=models.PROTECT)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = 'Cities'

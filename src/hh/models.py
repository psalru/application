from django.db import models
from config.models import BaseModel
from geo.models import FederalRegion
from university.models import University


class HHUniversity(BaseModel):
    university = models.ForeignKey(University, related_name='hh', on_delete=models.PROTECT, help_text='Ссылка на университет')
    employer_id = models.IntegerField(null=True, blank=True, help_text='ID организации как работодателя для работы с HH API')
    educational_institution_id = models.IntegerField(null=True, blank=True, help_text='ID организации как обр. организации для работы с HH API')

    def __str__(self):
        return self.university.title

    class Meta:
        db_table = 'hh_hh_university'
        verbose_name_plural = 'HH universities'


class CurrencyExchangeRate(BaseModel):
    date = models.DateField(help_text='Дата курса обмена валюты')
    title = models.CharField(max_length=255, help_text='Название валюты')
    nominal = models.IntegerField(help_text='Номинал (сколько в рублях)')
    value = models.FloatField(help_text='Курс обмена (сколько можно получить в валюте за номинал)')
    char_code = models.CharField(max_length=3, help_text='Текстовый код из 3-х символов')
    num_code = models.IntegerField(help_text='Номерной код валюты')
    currency_id = models.CharField(max_length=10, help_text='ID валюты (указано в атрибуте тега валюты в XML)')

    def __str__(self):
        return f'{self.date}: {self.title} - {self.nominal}'

    class Meta:
        db_table = 'hh_currency_exchange_rate'


class Vacancy(BaseModel):
    hh_university = models.ForeignKey(HHUniversity, on_delete=models.PROTECT, help_text='Ссылка на HH университет')
    hh_id = models.IntegerField(help_text='ID вакансии в HH')
    hh_created_at = models.DateTimeField(help_text='Дата и время публикации вакансии')
    hh_initial_created_at = models.DateTimeField(help_text='Дата и время создания вакансии')
    title = models.CharField(max_length=255, help_text='Наименование вакансии')
    description = models.TextField(help_text='Описание вакансии')
    salary_from = models.FloatField(null=True, blank=True, help_text='Заработная плата «от»')
    salary_to = models.FloatField(null=True, blank=True, help_text='Заработная плата «до»')
    salary_currency = models.CharField(max_length=3, null=True, blank=True, help_text='3-х символьный код валюты (принудительно приводится к RUR)')
    salary_gross = models.BooleanField(null=True, blank=True, help_text='Признак того что оклад указан до вычета налогов')
    experience = models.CharField(max_length=25, help_text='Требуемый опыт работы (без нормализации)')
    schedule = models.CharField(max_length=25, help_text='График работы (без нормализации)')
    employment = models.CharField(max_length=25, help_text='Тип занятости (без нормализации)')
    federal_region = models.ForeignKey(FederalRegion, null=True, blank=True, on_delete=models.PROTECT, help_text='Ссылка на регион РФ')
    url = models.CharField(max_length=255, help_text='Ссылка на страницу вакансии на HH')
    s3_bucket = models.CharField(max_length=255, help_text='Баккет в S3')
    s3_key = models.CharField(max_length=255, help_text='Ссылка на JSON вакансии полученный от HH')

    def __str__(self):
        return self.title

    class Meta:
        db_table = 'hh_vacancy'
        verbose_name_plural = 'Vacancies'


class ProfessionalRole(BaseModel):
    vacancy = models.ForeignKey(Vacancy, related_name='professional_role', on_delete=models.PROTECT, help_text='Ссылка на вакансию')
    hh_professional_role_dict_id = models.IntegerField(help_text='Ссылка на справочник профессиональных ролей в HH')
    title = models.CharField(max_length=255, help_text='Название ключевого навыка')

    def __str__(self):
        return self.title

    class Meta:
        db_table = 'hh_professional_role'


class Skill(BaseModel):
    vacancy = models.ForeignKey(Vacancy, related_name='skill', on_delete=models.PROTECT, help_text='Ссылка на вакансию')
    title = models.CharField(max_length=255, help_text='Название ключевого навыка')

    def __str__(self):
        return self.title

from rest_framework import serializers

from .models import Vacancy


class VacancyFeedSerializer(serializers.ModelSerializer):
    s3 = serializers.SerializerMethodField('get_s3')
    professional_role = serializers.StringRelatedField(many=True)
    skill = serializers.StringRelatedField(many=True)

    class Meta:
        model = Vacancy
        exclude = ['s3_bucket', 's3_key']

    def get_s3(self, obj):
        return f"https://storage.yandexcloud.net/{obj.s3_bucket}/{obj.s3_key}" if obj.s3_key else None

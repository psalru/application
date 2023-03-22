from rest_framework import serializers

from .models import Vacancy


class VacancyFeedSerializer(serializers.ModelSerializer):
    professional_role = serializers.StringRelatedField(many=True)
    skill = serializers.StringRelatedField(many=True)

    class Meta:
        model = Vacancy
        fields = '__all__'

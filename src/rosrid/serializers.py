from rest_framework import serializers

from .models import Active, ActiveType
from dict.serializers import OECDSerializer


class ActiveTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = ActiveType
        fields = '__all__'


class ActiveSerializer(serializers.ModelSerializer):
    type = ActiveTypeSerializer()
    oecd = OECDSerializer(many=True)

    class Meta:
        model = Active
        fields = '__all__'

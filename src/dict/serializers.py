from rest_framework import serializers

from .models import OECDGroup, OECD


class OECDGroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = OECDGroup
        fields = '__all__'


class OECDSerializer(serializers.ModelSerializer):
    oecd_group = OECDGroupSerializer()

    class Meta:
        model = OECD
        fields = '__all__'

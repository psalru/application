from rest_framework import serializers

from .models import FederalDistrict, FederalRegion, City


class FederalDistrictSerializer(serializers.ModelSerializer):
    class Meta:
        model = FederalDistrict
        fields = '__all__'


class FederalRegionSerializer(serializers.ModelSerializer):
    class Meta:
        model = FederalRegion
        fields = '__all__'


class CitySerializer(serializers.ModelSerializer):
    class Meta:
        model = City
        fields = '__all__'

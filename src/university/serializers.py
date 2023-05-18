from rest_framework import serializers

from hh.models import HHUniversity
from rosrid.models import RosridUniversity
from .models import University, UniversityStatus, Status


class HHUniversitySerializer(serializers.ModelSerializer):
    class Meta:
        model = HHUniversity
        fields = ['id', 'employer_id', 'educational_institution_id']


class RosridUniversitySerializer(serializers.ModelSerializer):
    class Meta:
        model = RosridUniversity
        fields = ['id', 'rosrid_id']


class StatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = Status
        fields = '__all__'


class UniversityStatusSerializer(serializers.ModelSerializer):
    status = serializers.StringRelatedField()

    class Meta:
        model = UniversityStatus
        fields = ['status_id', 'status', 'start', 'end']


class UniversitySerializer(serializers.ModelSerializer):
    hh = HHUniversitySerializer(many=True)
    rosrid = RosridUniversitySerializer(many=True)
    statuses = UniversityStatusSerializer(many=True)

    class Meta:
        model = University
        fields = '__all__'

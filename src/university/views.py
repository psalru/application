from rest_framework import viewsets

from .models import University, Status
from .serializers import UniversitySerializer, StatusSerializer


class StatusViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Status.objects.all().order_by('id')
    serializer_class = StatusSerializer


class UniversityViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = University.objects.all().order_by('id')
    serializer_class = UniversitySerializer

from rest_framework import viewsets

from .models import University
from .serializers import UniversitySerializer


class UniversityViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = University.objects.all()
    serializer_class = UniversitySerializer

from rest_framework import viewsets

from .models import Vacancy
from .serializers import VacancyFeedSerializer


class VacancyViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Vacancy.objects.order_by('-hh_id', 'created_at').distinct('hh_id')
    serializer_class = VacancyFeedSerializer
    filterset_fields = {
        'hh_initial_created_at': ['gte', 'lte'],
        'hh_university': ['exact']
    }



from rest_framework import viewsets

from .models import NewsFeed
from .serializers import NewsFeedSerializer


class NewsFeedViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = NewsFeed.objects.all().order_by('id')
    serializer_class = NewsFeedSerializer
    filterset_fields = {
        'date': ['exact', 'gte', 'lte'],
        'domain': ['exact']
    }

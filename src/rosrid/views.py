from rest_framework import viewsets

from .models import Active
from .serializers import ActiveSerializer


class ActiveViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Active.objects.all().order_by('id')
    serializer_class = ActiveSerializer

from rest_framework import viewsets

from .models import OECD
from .serializers import OECDSerializer


class OECDViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = OECD.objects.all().order_by('id')
    serializer_class = OECDSerializer

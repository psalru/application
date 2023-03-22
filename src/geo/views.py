from rest_framework import viewsets

from .models import FederalDistrict, FederalRegion, City
from .serializers import FederalDistrictSerializer, FederalRegionSerializer, CitySerializer


class FederalDistrictViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = FederalDistrict.objects.all().order_by('id')
    serializer_class = FederalDistrictSerializer


class FederalRegionViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = FederalRegion.objects.all().order_by('id')
    serializer_class = FederalRegionSerializer


class CityViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = City.objects.all().order_by('id')
    serializer_class = CitySerializer

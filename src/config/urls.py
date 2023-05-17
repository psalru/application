from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from django.views.generic.base import RedirectView

from geo.views import FederalDistrictViewSet, FederalRegionViewSet, CityViewSet
from university.views import UniversityViewSet, StatusViewSet
from google_alerts.views import NewsFeedViewSet
from hh.views import VacancyViewSet
from dict.views import OECDViewSet

router_api = routers.DefaultRouter()
router_api.register(r'district', FederalDistrictViewSet)
router_api.register(r'region', FederalRegionViewSet)
router_api.register(r'city', CityViewSet)
router_api.register(r'university', UniversityViewSet)
router_api.register(r'status', StatusViewSet)
router_api.register(r'newsfeed', NewsFeedViewSet)
router_api.register(r'vacancy', VacancyViewSet)
router_api.register(r'oecd', OECDViewSet)

urlpatterns = [
    path('', RedirectView.as_view(url='api/', permanent=False)),
    path('admin/', admin.site.urls),
    path('api/', include(router_api.urls))
]

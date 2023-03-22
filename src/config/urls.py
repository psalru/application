"""config URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from django.views.generic.base import RedirectView

from geo.views import FederalDistrictViewSet, FederalRegionViewSet, CityViewSet
from university.views import UniversityViewSet, StatusViewSet

router_api = routers.DefaultRouter()
router_api.register(r'district', FederalDistrictViewSet)
router_api.register(r'region', FederalRegionViewSet)
router_api.register(r'city', CityViewSet)
router_api.register(r'university', UniversityViewSet)
router_api.register(r'status', StatusViewSet)

urlpatterns = [
    path('', RedirectView.as_view(url='api/', permanent=False)),
    path('admin/', admin.site.urls),
    path('api/', include(router_api.urls))
]

from django.contrib import admin
from .models import *


class FederalDistrictAdmin(admin.ModelAdmin):
    list_display = ['id', 'short_title', 'title', 'capital', 'square']
    list_display_links = ['id', 'title', 'short_title']
    search_fields = ['title', 'short_title', 'capital']
    ordering = ('title',)


class FederalRegionAdmin(admin.ModelAdmin):
    list_display = ['id', 'type', 'title', 'capital', 'square']
    list_display_links = ['id', 'title']
    search_fields = ['title', 'capital']
    ordering = ('title',)


class CityAdmin(admin.ModelAdmin):
    list_display = ['title', 'federal_district', 'federal_region']
    search_fields = ['title']
    ordering = ('title',)


admin.site.register(FederalDistrict, FederalDistrictAdmin)
admin.site.register(FederalRegion, FederalRegionAdmin)
admin.site.register(City, CityAdmin)

from .models import *
from django.contrib import admin


class UniversityAdmin(admin.ModelAdmin):
    list_display = ['mon_id', 'title_display', 'domain']
    list_display_links = ['mon_id', 'title_display']
    search_fields = ['id', 'mon_id', 'title', 'title_short', 'title_display']
    ordering = ('mon_id', 'id')


class StatusAdmin(admin.ModelAdmin):
    list_display = ['id', 'title']
    list_display_links = ['id', 'title']
    search_fields = ['id', 'title']
    ordering = ('id',)


class UniversityStatusAdmin(admin.ModelAdmin):
    list_display = ['id', 'start', 'end', 'status', 'university']
    list_display_links = ['id', 'status', 'university']
    search_fields = ['id', 'status', 'university']
    ordering = ('start', 'id')


admin.site.register(University, UniversityAdmin)
admin.site.register(Status, StatusAdmin)
admin.site.register(UniversityStatus, UniversityStatusAdmin)

from .models import *
from django.contrib import admin


class OECDGroupAdmin(admin.ModelAdmin):
    list_display = ['code', 'title']
    list_display_links = ['code', 'title']
    search_fields = ['code', 'title', 'title_src']
    ordering = ('code', 'id')


class OECDAdmin(admin.ModelAdmin):
    list_display = ['code', 'title']
    list_display_links = ['code', 'title']
    search_fields = ['code', 'title', 'title_src']
    ordering = ('code', 'id')


admin.site.register(OECDGroup, OECDGroupAdmin)
admin.site.register(OECD, OECDAdmin)

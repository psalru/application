from django.contrib import admin
from .models import NewsFeed


class NewsFeedAdmin(admin.ModelAdmin):
    list_display = ('id', 'date', 'domain', 'title')
    list_display_links = ('id', 'title')
    search_fields = ('id', 'title')


admin.site.register(NewsFeed, NewsFeedAdmin)

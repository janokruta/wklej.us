from django.contrib import admin

from links.models import Link


class LinkAdmin(admin.ModelAdmin):
    list_display = ['slug', 'timestamp']
    search_fields = ['slug']
    ordering = ['-timestamp']


admin.site.register(Link, LinkAdmin)

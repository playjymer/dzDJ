from django.contrib import admin
from .models import Advertisement


class AdvertisementAdmin(admin.ModelAdmin):
    list_display = ['title', 'content', 'created_at', 'updated_at']


admin.site.register(Advertisement, AdvertisementAdmin)
class AdvertisementAdmin(admin.ModelAdmin):
    list_display = ['title', 'content', 'created_at', 'updated_at_today']
    list_filter = ['created_at', 'updated_at']

    def updated_at_today(self, obj):
        if obj.updated_today():
            return f'<span style="color: green;">Сегодня в {obj.updated_at.time()}</span>'
        else:
            return obj.updated_at
    updated_at_today.allow_tags = True
    updated_at_today.short_description = 'Последнее обновление'

admin.site.register(Advertisement, AdvertisementAdmin)

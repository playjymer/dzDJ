from django.contrib import admin
from .models import OnlineShop
from django.utils.html import format_html

@admin.register(OnlineShop)
class OnlineShopAdmin(admin.ModelAdmin):
    list_display = ('title', 'display_thumbnail')  # Замените 'title' на поля вашей модели

    def display_thumbnail(self, obj):
        thumbnail_url = obj.get_thumbnail_url()
        return format_html('<img src="{}" width="50" height="50" />', thumbnail_url)
    display_thumbnail.short_description = 'Thumbnail'
# Register your models here.

# создаем класс для отображения модели в панели администрирования
class OnlineShopAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'description', 'price', 'created_time', 'auction', 'image']
    list_filter = ['auction', 'created_time']
    actions = ['make_auction_as_false', 'make_auction_as_true']

    fieldsets = (
        ('Общее', {
            'fields': ('title', 'description', 'image')
        }),
        ('Финансы', {
            'fields': ('price', 'auction'),
            'classes': ['collapse']
        })

    )

    @admin.action(description='Убрать возможность торга')
    # request - запрос с сайта
    # queryset - набор объектов, к которым применится созданный метод
    def make_auction_as_false(self, request, queryset):
        queryset.update(auction=False)

    @admin.action(description='Добавить возможность торга')
    def make_auction_as_true(self, request, queryset):
        queryset.update(auction=True)

    def get_thumbnail_url(self):
        if self.image:
        # Здесь вы должны определить логику получения URL уменьшенной копии картинки
            return self.image.url  # Вернуть URL уменьшенной копии
        else:
            return '/static/img/adv.png'  # Вернуть URL статической картинки по умолчанию

    
# отображаем нашу модель в панели администрирования
admin.site.register(OnlineShop, OnlineShopAdmin)
from django.db import models
from django.utils import timezone

# Create your models here.

class OnlineShop(models.Model):
    title = models.CharField('Заголовок', max_length=128)
    description = models.TextField('Описание')
    price = models.DecimalField('Цена', max_digits=10, decimal_places=2)
    auction = models.BooleanField('Торг', help_text='Отметьте уместен ли торг?')
    created_time = models.DateTimeField(auto_now_add=True)
    update_time = models.DateTimeField(auto_now=True)

class Advertisement(models.Model):
    # Ваши поля модели объявления, например:
    title = models.CharField(max_length=100)
    content = models.TextField()
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)

    def updated_today(self):
        return self.updated_at.date() == timezone.now().date()    
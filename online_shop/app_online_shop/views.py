from django.shortcuts import render
# подключаем объект для выполнения http-запросов
from django.http import HttpResponse
from .models import OnlineShop
# Create your views here.

# функция, отображающая файл index.html
def index(request):
    online_shops = OnlineShop.objects.all()
    context = {'online_shops': online_shops}
    return render(request, 'index.html', context)

# функция, отображающая файл top-sellers.html
def top_sellers(request):
    return render(request, 'top-sellers.html')
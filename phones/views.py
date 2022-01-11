import csv
from datetime import datetime

from django.core.exceptions import ObjectDoesNotExist
from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render, redirect
# from phones.management.commands.import_phones import Command
from django.urls import reverse

# def index(request):
#     return redirect('catalog')
from phones.models import Phone


def index(request):
    """
    Функция показа домашней страницы
    """
    template = 'index.html'
    pages = {
        'Домашняя страница': reverse('index'),
        'Каталог телефонов': reverse('catalog')
    }
    context = {
        'pages': pages
    }

    return render(request, template, context)


def show_catalog(request):
    """
    Функция принимает данные из БД Phone.objects, сотрирует данные и выдает слварь с данными context шаблону template
    """
    template = 'catalog.html'

    sort = request.GET.get('sort', '')
    if sort == 'name':
        phones = Phone.objects.order_by("name")
    elif sort == 'min_price':
        phones = Phone.objects.order_by("price")
    elif sort == 'max_price':
        phones = Phone.objects.order_by("-price")
    else:
        phones = Phone.objects.all()
    context = {'phones': phones}
    return render(request, template, context)


def show_phones(response):
    """
    Функция для тестового вывода данных из БД Phone.objects.all
    """

    phones_objects = Phone.objects.all()
    phones = [f'{p.id}, {p.name}, {p.price}, {p.image}, {p.release_date}, {p.lte_exists}, {p.slug}' for p in
              phones_objects]
    return HttpResponse('<br>'.join(phones))


def show_product(request, slug):
    """
    Функция отображения данных о выбранном товаре. Через slug получает выбранную модель
    Отображается на странице product.html
    """
    template = 'product.html'

    try:
        phone = Phone.objects.get(slug=slug)
    except ObjectDoesNotExist:
        return HttpResponseNotFound("Phone does not exist")

    context = {'phone': phone}

    return render(request, template, context)

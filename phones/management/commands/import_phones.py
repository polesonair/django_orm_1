import csv

from django.core.management.base import BaseCommand
from phones.models import Phone


class Command(BaseCommand):
    def add_arguments(self, parser):
        pass

    def handle(self, *args, **options):
        with open('phones.csv') as f:
            phones_list = csv.DictReader(f, delimiter=';')
            for p in phones_list:
                print('phones_list', p)
                phone = Phone(id=p.get('id'), name=p.get('name'), price=int(p.get('price')), image=p.get('image'),
                              release_date=p.get('release_date'), lte_exists=bool(p.get('lte_exists')),
                              slug=p.get('name'))
                phone.save()

from django.db import models
from django.utils import timezone


class Phone(models.Model):
    # TODO: Добавьте требуемые поля
    name = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=7, decimal_places=2)
    image = models.ImageField(null=True)
    release_date = models.DateField(default=timezone.now)
    lte_exists = models.BooleanField(null=True)
    slug = models.SlugField(null=True)

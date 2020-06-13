from django.db import models
from datetime import date

class Category(models.Model):
    title = models.CharField("Категория", max_length=50)
    description = models.TextField("Описание категории", blank=True)
    url = models.SlugField(max_length=200, unique=True)
    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"


class Writer(models.Model):
    name = models.CharField("Автор", max_length=250)
    description = models.TextField("Информация об авторе", blank=True)
    class Meta:
        verbose_name = "Автор"
        verbose_name_plural = "Авторы"


class Product(models.Model):
    title = models.CharField("Книга", max_length=50)
    description = models.TextField("Описание книги", blank=True)
    category = models.ManyToManyField(Category, verbose_name="Категория", related_name="category_product")
    writer = models.ManyToManyField(Writer, verbose_name="Автор", related_name="writer_product")
    url = models.SlugField(max_length=200, unique=True)
    sku = models.CharField("Артикул", max_length=10, unique=True)
    date_create = models.DateField("Дата создания")
    price = models.DecimalField("Цена", decimal_places=2, max_digits=5, default=0)
    stock = models.PosiiveIntegerField("Количество на складе", default=1)
    status = models.CharField("Статус на сайте", max_length=20, choices=STATUS_CHOICES, default="Enable")
    class Meta:
        verbose_name = "Книга"
        verbose_name_plural = "Книги"
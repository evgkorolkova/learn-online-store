from datetime import datetime
from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone
from django.conf import settings

class Profile(models.Model):

    user = models.OneToOneField(
        User,
        related_name='Профиль',
        default=1,
        on_delete=models.PROTECT
    )


def create_user_callback(sender, instance, created, **kwargs):
    if created:
        Profile.objects.get_or_create(user=instance)


class Order(models.Model):
    delivery_address = models.CharField(
        verbose_name='Адрес и дом',
        max_length=128,
        default=None,
        blank=True,
        null=True
    )
    delivery_address_house_part = models.CharField(
        verbose_name='Подъезд',
        max_length=128,
        default=None,
        blank=True,
        null=True
    )    
    delivery_apart = models.CharField(
        verbose_name='Квартира / Офис',
        max_length=128,
        default=None,
        blank=True,
        null=True
    )
    create_at = models.DateTimeField(auto_now_add=True)
    phone_number = models.CharField(
        verbose_name='Номер телефона',
        max_length=15,
        default=None,
        null=True,
        blank=False
    )
    order_number = models.IntegerField() #Нужен ли? Можно использовать для хранение трек номера посылки          


class Category(models.Model):
    title = models.CharField("Категория", max_length=50)
    description = models.TextField("Описание категории", blank=True, null=True)
    url = models.SlugField(max_length=200, unique=True)
    
    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"
    
    def __str__(self):
        return self.title



class Writer(models.Model):
    name = models.CharField("Автор", max_length=250)
    description = models.TextField("Информация об авторе", blank=True, null=True)
    
    class Meta:
        verbose_name = "Автор"
        verbose_name_plural = "Авторы"
    
    def __str__(self):
        return self.name


class Product(models.Model):
    STATUS_CHOICES = (
        ("yes", "Enable"),
        ("no", "Disable")   
        )

    title = models.CharField("Книга", max_length=50)
    description = models.TextField("Описание книги", blank=True, null=True)
    category = models.ManyToManyField(Category, verbose_name="Категория", related_name="category_product")
    writer = models.ForeignKey(Writer, verbose_name="Автор", related_name="writer_product", on_delete=models.SET_NULL, null=True)
    url = models.SlugField(max_length=200, unique=True)
    sku = models.CharField("Артикул", max_length=10, unique=True)
    date_create = models.DateTimeField("Дата создания", auto_now_add=True, null=True)
    price = models.DecimalField("Цена", decimal_places=2, max_digits=5, default=0)
    stock = models.PositiveIntegerField("Количество на складе", default=1)
    status = models.CharField("Статус на сайте", max_length=20, choices=STATUS_CHOICES, default="yes")
    img = models.ImageField(verbose_name="Иозображение книги", upload_to='', null=True, blank=True, default='no_image_given_128_128.jpg')

    class Meta:
        verbose_name = "Книга"
        verbose_name_plural = "Книги"

    def __str__(self):
        return self.title

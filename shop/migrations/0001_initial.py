# Generated by Django 2.2.13 on 2020-06-13 16:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='Категория')),
                ('description', models.TextField(blank=True, null=True, verbose_name='Описание категории')),
                ('url', models.SlugField(max_length=200, unique=True)),
            ],
            options={
                'verbose_name': 'Категория',
                'verbose_name_plural': 'Категории',
            },
        ),
        migrations.CreateModel(
            name='Writer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250, verbose_name='Автор')),
                ('description', models.TextField(blank=True, null=True, verbose_name='Информация об авторе')),
            ],
            options={
                'verbose_name': 'Автор',
                'verbose_name_plural': 'Авторы',
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='Книга')),
                ('description', models.TextField(blank=True, null=True, verbose_name='Описание книги')),
                ('url', models.SlugField(max_length=200, unique=True)),
                ('sku', models.CharField(max_length=10, unique=True, verbose_name='Артикул')),
                ('date_create', models.DateField(verbose_name='Дата создания')),
                ('price', models.DecimalField(decimal_places=2, default=0, max_digits=5, verbose_name='Цена')),
                ('stock', models.PositiveIntegerField(default=1, verbose_name='Количество на складе')),
                ('status', models.CharField(choices=[('yes', 'Enable'), ('no', 'Disable')], default='yes', max_length=20, verbose_name='Статус на сайте')),
                ('category', models.ManyToManyField(related_name='category_product', to='shop.Category', verbose_name='Категория')),
                ('writer', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='writer_product', to='shop.Writer', verbose_name='Автор')),
            ],
            options={
                'verbose_name': 'Книга',
                'verbose_name_plural': 'Книги',
            },
        ),
    ]

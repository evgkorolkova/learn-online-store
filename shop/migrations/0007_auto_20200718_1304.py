# Generated by Django 2.2.14 on 2020-07-18 08:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0006_auto_20200718_1250'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='img',
            field=models.ImageField(blank=True, default='no_image_given_128_128.jpg', null=True, upload_to='', verbose_name='Иозображение книги'),
        ),
    ]

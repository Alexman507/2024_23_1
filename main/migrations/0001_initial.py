# Generated by Django 5.0.4 on 2024-05-20 06:50

import django.db.models.deletion
import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Введите название категории', max_length=250, verbose_name='Название')),
                ('description', models.TextField(blank=True, help_text='Введите описание категории', null=True, verbose_name='Описание')),
            ],
            options={
                'verbose_name': 'категория',
                'verbose_name_plural': 'категории',
            },
        ),
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Введите имя', max_length=50, verbose_name='Имя')),
                ('phone', models.CharField(help_text='Введите телефон', max_length=20, verbose_name='Телефон')),
                ('message', models.TextField(blank=True, help_text='Введите сообщение', null=True, verbose_name='Сообщение')),
                ('created_at', models.DateTimeField(blank=True, default=django.utils.timezone.now, help_text='Введите дату создания', null=True, verbose_name='Дата создания')),
            ],
            options={
                'verbose_name': 'Контакт',
                'verbose_name_plural': 'Контакты',
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Введите наименование', max_length=250, verbose_name='Наименование')),
                ('description', models.TextField(blank=True, help_text='Введите описание', null=True, verbose_name='Описание')),
                ('preview', models.ImageField(blank=True, help_text='Загрузите изображение', null=True, upload_to='product/photo', verbose_name='Превью')),
                ('price', models.DecimalField(decimal_places=2, help_text='Введите цену', max_digits=9, verbose_name='Цена')),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now, help_text='Введите дату создания', verbose_name='Дата создания')),
                ('updated_at', models.DateTimeField(auto_now_add=True, help_text='Введите дату изменения', verbose_name='Дата последнего изменения')),
                ('category', models.ForeignKey(help_text='Введите категорию', on_delete=django.db.models.deletion.CASCADE, related_name='categories', to='main.category', verbose_name='Категория')),
            ],
            options={
                'verbose_name': 'Продукт',
                'verbose_name_plural': 'Продукты',
                'ordering': ['category', 'name'],
            },
        ),
    ]
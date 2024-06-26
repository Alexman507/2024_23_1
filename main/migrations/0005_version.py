# Generated by Django 5.0.6 on 2024-06-10 08:27

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_alter_contact_address_alter_contact_inn'),
    ]

    operations = [
        migrations.CreateModel(
            name='Version',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.PositiveIntegerField(help_text='укажите номер версии', verbose_name='Номер версии')),
                ('name', models.CharField(help_text='Введите название версии', max_length=100, verbose_name='Название версии')),
                ('sign', models.BooleanField(verbose_name='Признак текущей версии')),
                ('product', models.ForeignKey(help_text='название продукта', on_delete=django.db.models.deletion.CASCADE, related_name='product', to='main.product', verbose_name='продукт')),
            ],
            options={
                'verbose_name': 'Версия',
                'verbose_name_plural': 'Версии',
                'ordering': ['number', 'name'],
            },
        ),
    ]
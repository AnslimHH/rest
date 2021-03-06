# Generated by Django 4.0.4 on 2022-06-04 09:29

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sender', models.CharField(max_length=100, verbose_name='Отправитель')),
                ('senders_address', models.CharField(max_length=150, verbose_name='Адрес отправителя')),
                ('shipped_item', models.CharField(max_length=150, verbose_name='Отправленный товар')),
                ('FIO', models.CharField(max_length=250, verbose_name='ФИО')),
                ('email', models.CharField(max_length=100, verbose_name='Email')),
                ('phone_number', models.CharField(max_length=11, verbose_name='Номер телефона')),
                ('address_recipient', models.CharField(max_length=150, verbose_name='Адрес получателя')),
            ],
            options={
                'verbose_name': 'Заказ',
                'verbose_name_plural': 'Заказы',
            },
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('surname', models.CharField(max_length=60, verbose_name='Фамилия')),
                ('name', models.CharField(max_length=25, verbose_name='Имя')),
                ('patronymic', models.CharField(max_length=45, verbose_name='Отчество')),
                ('email', models.CharField(max_length=100, verbose_name='Email')),
                ('phone_number', models.CharField(max_length=11, verbose_name='Номер телефона')),
                ('password', models.CharField(max_length=150, verbose_name='Пароль')),
            ],
            options={
                'verbose_name': 'Пользователь',
                'verbose_name_plural': 'Пользователи',
            },
        ),
    ]

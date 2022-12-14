# Generated by Django 4.1.1 on 2022-10-02 19:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='location',
            name='lat',
            field=models.DecimalField(decimal_places=6, max_digits=8, verbose_name='Широта'),
        ),
        migrations.AlterField(
            model_name='location',
            name='log',
            field=models.DecimalField(decimal_places=6, max_digits=8, verbose_name='Долгота'),
        ),
        migrations.AlterField(
            model_name='location',
            name='name',
            field=models.CharField(max_length=100, verbose_name='Локация'),
        ),
        migrations.AlterField(
            model_name='user',
            name='age',
            field=models.PositiveSmallIntegerField(help_text='Введите Ваш возраст', verbose_name='Возраст'),
        ),
        migrations.AlterField(
            model_name='user',
            name='first_name',
            field=models.CharField(help_text='Введите имя пользователя до 20 знаков', max_length=60, verbose_name='Имя'),
        ),
        migrations.AlterField(
            model_name='user',
            name='last_name',
            field=models.CharField(help_text='Введите фамилию пользователя до 30 знаков', max_length=80, verbose_name='Фамилия'),
        ),
        migrations.AlterField(
            model_name='user',
            name='password',
            field=models.CharField(help_text='Введите пароль не менее 8 знаков', max_length=30, verbose_name='Пароль'),
        ),
        migrations.AlterField(
            model_name='user',
            name='username',
            field=models.CharField(help_text='Введите Ваш никнейм до 20 знаков', max_length=20, unique=True, verbose_name='Никнейм'),
        ),
    ]

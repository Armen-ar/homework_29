from django.db import models

from users.models import User


class Category(models.Model):
    name = models.CharField(
        verbose_name="Название категории",
        max_length=60,
        unique=True
    )

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"

    def __str__(self):
        return self.name


class Ad(models.Model):
    name = models.CharField(
        verbose_name="Тема объявления",
        max_length=50
    )
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='ads',
    )
    price = models.PositiveIntegerField(
        verbose_name="Цена"
    )
    description = models.TextField(
        verbose_name="Текст объявления",
        null=True
    )
    is_published = models.BooleanField(
        verbose_name="Публикация",
        default=False
    )
    image = models.ImageField(
        verbose_name="Фото",
        upload_to='pictures',
        null=True, blank=True
    )
    category = models.ForeignKey(
        Category,
        null=True,
        on_delete=models.CASCADE,
        related_name='ads'
    )

    class Meta:
        verbose_name = "Объявление"
        verbose_name_plural = "Объявления"

    def __str__(self):
        return self.name

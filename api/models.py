from django.db import models
from filer.fields.image import FilerImageField


class Slider(models.Model):
    title = models.CharField(
        max_length=25,
        verbose_name='Название'
    )
    description = models.TextField(
        verbose_name='Описание'
    )
    image = FilerImageField(
        related_name='slider_image',
        on_delete=models.CASCADE,
        verbose_name='Изображение'
    )
    order = models.IntegerField(
        default=0,
        verbose_name='Сортировка'
    )
    show = models.BooleanField(
        default=True,
        verbose_name='Видимость'
    )

    class Meta:
        ordering = ['order']
        verbose_name = 'Слайд'
        verbose_name_plural = 'Слайды'

    def __str__(self):
        return self.title, self.description
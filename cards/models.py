from django.db import models


class Category(models.Model):
    title = models.CharField('Название категории', max_length=50)
    icon = models.ImageField('Иконка', upload_to='category/icon')
    icon_mobile = models.ImageField('Иконка', upload_to='category/icon_mobile')
    ordering = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['ordering']

    def __str__(self):
        return self.title

class Item(models.Model):
    image = models.ImageField('изображение товара', upload_to='item')
    price = models.CharField('цена', max_length=20)
    category = models.ForeignKey(Category, on_delete=models.PROTECT, related_name='item')
    like = models.BooleanField('Нравится', default=False)
    description = models.TextField('Описание')
    create_at = models.DateTimeField('вРЕМЯ создания')
    ordering = models.PositiveIntegerField(default=0)

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'
        ordering = ['ordering']


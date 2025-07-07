from django.core.validators import MinValueValidator
from django.db import models

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=50, unique=True, verbose_name='Имя')
    content = models.TextField(verbose_name='Контент')

    def __str__(self):
        return f"{self.id} - {self.name}"

    class Meta:
        db_table = 'category_db'
        verbose_name = 'Категория'
        verbose_name_plural = "Категории"

class Product(models.Model):
    title = models.CharField(max_length=50,verbose_name='Название', null=False, blank=False)
    description = models.TextField(verbose_name='Описание', null=True, blank=True)
    category  = models.ForeignKey('webapp.Category', on_delete=models.RESTRICT, verbose_name='Категория', related_name='products', null=False, blank=False)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    price = models.DecimalField(decimal_places=2, max_digits=7, verbose_name='Цена', null=False, blank=False)
    image = models.URLField(verbose_name='Фото', null=False, blank=False)
    remaining = models.IntegerField(verbose_name='Остаток', null=False, blank=False, validators=[MinValueValidator(0)], default=1)

    def __str__(self):
        return f"{self.id} - {self.title}"

    class Meta:
        db_table = 'product_db'
        verbose_name = 'Продукт'
        verbose_name_plural = "Продукты"
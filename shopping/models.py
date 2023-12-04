from django.db import models

class Category(models.Model):
    name = models.CharField(verbose_name='カテゴリ名', max_length=64)

    def __str__(self):
        return self.name


class Item(models.Model):
    name = models.CharField(verbose_name='商品名', max_length=64)
    price = models.IntegerField(verbose_name='商品価格', default=0)
    description = models.TextField(verbose_name='商品説明', max_length=256)
    image = models.ImageField(verbose_name='商品画像', default=None, blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
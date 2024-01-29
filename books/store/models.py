from django.db import models


class Book(models.Model):
    def __str__(self):
        return f"ID {self.id}: {self.name}"

    name = models.CharField(max_length=255)
    price = models.DecimalField(
        max_digits=6,
        decimal_places=2,
    )  # Указываем кол-во разрядов, кол-во знаков после запятой

from statistics import quantiles
from tkinter import Menu
from django.db import models

# Create your models here.
class Ingridient(models.Model):
    KILOGRAM = 'KG'
    GRAM = 'G'
    MILIGRAM = 'MG'
    LITER = 'L'
    MILILITER = 'ML'
    PIECE = 'PC'
    TABLESPOON = 'TS'
    TEASPOON = 'TE'
    UNIT_CHOICES = [
        (KILOGRAM, 'kg'),
        (GRAM, 'g'),
        (LITER, 'l'),
        (MILILITER, 'ml'),
        (MILIGRAM, 'mg'),
        (PIECE, 'piece/s'),
        (TABLESPOON, 'table spoon'),
        (TEASPOON, 'tea spoon'),
    ]
    name = models.CharField(max_length=100)
    quantity = models.DecimalField(max_digits=8, decimal_places=4)
    unit = models.CharField(max_length=2, choices=UNIT_CHOICES)
    unit_price = models.DecimalField(max_digits=6, decimal_places=2)

    def __str__(self) -> str:
        return self.name


class MenuItem(models.Model):
    title = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    def __str__(self) -> str:
        return self.title

class RecipeRequirement(models.Model):
    menu_item = models.ForeignKey(MenuItem, on_delete=models.CASCADE)
    ingridient = models.ForeignKey(Ingridient, on_delete=models.CASCADE)
    quantity = models.DecimalField(max_digits=8, decimal_places=4)
    def __str__(self) -> str:
        return f'{self.ingridient}_{self.quantity}'


class Purchase(models.Model):
    menu_item = models.ForeignKey(MenuItem, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)


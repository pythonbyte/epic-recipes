from django.db import models



class Ingredient(models.Model):
    GRAMS = 'G'
    KILOGRAMS = 'KG'
    LITER = 'L'
    CENTILITER = 'CL'
    UNIT_TYPES = (
        (GRAMS, 'Grams (g)'),
        (KILOGRAMS, 'Kilograms (kg)'),
        (LITER, 'Liter (L)'),
        (CENTILITER, 'Centiliter (cl)'),
    )
    name = models.CharField(max_length=200, null=False, blank=False)
    article_number = models.CharField(max_length=13, null=False, blank=False, unique=True)
    cost = models.DecimalField(max_digits=6, decimal_places=2)
    amount = models.PositiveIntegerField()
    unit = models.CharField(max_length=200, null=False, blank=False, choices=UNIT_TYPES)


    def __str__(self):
        return f'{self.name} - {self.article_number}'
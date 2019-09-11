from django.db import models
from django.db.models.signals import post_save
from ingredientsapp.models import Ingredient
from .utils import convert_unit


class RecipeIngredient(models.Model):
    GRAMS = "G"
    KILOGRAMS = "KG"
    LITER = "L"
    CENTILITER = "CL"
    UNIT_TYPES = (
        (GRAMS, "Grams (g)"),
        (KILOGRAMS, "Kilograms (kg)"),
        (LITER, "Liter (L)"),
        (CENTILITER, "Centiliter (cl)"),
    )
    amount = models.PositiveIntegerField()
    unit = models.CharField(max_length=200, null=False, blank=False, choices=UNIT_TYPES)
    ingredient = models.ForeignKey(Ingredient, on_delete=models.CASCADE)
    cost = models.DecimalField(max_digits=6, decimal_places=2, default=0)

    def __str__(self):
        return f"{self.amount} {self.get_unit_display()} of {self.ingredient.name}"

    def save(self, *args, **kwargs):
        ingredient = self.ingredient
        self.cost = convert_unit(
            ingredient.cost, self.amount, ingredient.amount, self.unit, ingredient.unit
        )
        super(RecipeIngredient, self).save(*args, **kwargs)


def update_recipe_ingredients(sender, **kwargs):
    instance = kwargs["instance"]
    if instance:
        for i in instance.recipeingredient_set.all():
            i.save()


post_save.connect(update_recipe_ingredients, sender=Ingredient)


class Recipe(models.Model):
    name = models.CharField(max_length=200, null=False)
    preparation_time = models.PositiveIntegerField()
    ingredients = models.ManyToManyField(RecipeIngredient)
    image_file = models.ImageField(null=True)

    def __str__(self):
        return f"{self.name}"

    def recipe_cost(self):
        return sum([i.cost for i in self.ingredients.all()])

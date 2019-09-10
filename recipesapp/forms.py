from django import forms

from .models import Recipe, RecipeIngredient


class RecipeForm(forms.ModelForm):
    class Meta:
        model = Recipe
        exclude = ["ingredients"]


RecipeIngredientFormSet = forms.modelformset_factory(
    RecipeIngredient, exclude=("cost",), can_delete=True
)

from django import forms
from django.forms import BaseModelFormSet

from .models import Recipe, RecipeIngredient


class PillarRequiredFormSet(BaseModelFormSet):
    def clean(self):
        if any(self.errors):
            return
        for form in self.forms:
            ri_unit = form.cleaned_data["unit"]
            ingredient_unit = form.cleaned_data["ingredient"].unit
            if ri_unit in ("KG", "G") and ingredient_unit in ("L", "CL"):
                self.errors[0][
                    "unit_type"
                ] = " Invalid unit provided to the ingredient selected"
                return self.errors
            elif ri_unit in ("L", "CL") and ingredient_unit in ("KG", "G"):
                self.errors[0][
                    "unit_type"
                ] = " Invalid unit provided to the ingredient selected"
                return self.errors


class RecipeForm(forms.ModelForm):
    class Meta:
        model = Recipe
        exclude = ["ingredients"]


RecipeIngredientFormSet = forms.modelformset_factory(
    RecipeIngredient, formset=PillarRequiredFormSet, exclude=("cost",), can_delete=True
)

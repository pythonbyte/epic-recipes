from django.db import transaction
from django.db.models import Q
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from .models import Recipe, RecipeIngredient
from . forms import RecipeForm, RecipeIngredientFormSet


class RecipeList(ListView):
    model = Recipe
    paginate_by = 6
    ordering = ['-name']


class RecipeDetail(DetailView):
    model = Recipe


class RecipeCreate(CreateView):
    model = Recipe
    form_class = RecipeForm
    success_url = reverse_lazy('recipe_list')

    def get_context_data(self, **kwargs):
        context = super(RecipeCreate, self).get_context_data(**kwargs)
        if self.request.POST:
            context['formset'] = RecipeIngredientFormSet(self.request.POST)
        else:
            context['formset'] = RecipeIngredientFormSet(queryset=RecipeIngredient.objects.none())
        return context

    def form_valid(self, form):
        context = self.get_context_data()
        ingredients = context['formset']
        with transaction.atomic():
            self.object = form.save()
            if ingredients.is_valid():
                save_objects = ingredients.save()
                self.object.ingredients.set(save_objects)
        return super(RecipeCreate, self).form_valid(form)

class RecipeUpdate(UpdateView):
    form_class = RecipeForm
    model = Recipe
    success_url = reverse_lazy('recipe_list')

    def get_context_data(self, **kwargs):
        context = super(RecipeUpdate, self).get_context_data(**kwargs)
        if self.request.POST:
            context['formset'] = RecipeIngredientFormSet(self.request.POST)
        else:
            context['formset'] = RecipeIngredientFormSet(queryset=self.object.ingredients.all())
        return context

    def form_valid(self, form):
        context = self.get_context_data()
        ingredients = context['formset']
        with transaction.atomic():
            if ingredients.is_valid():
                save_objects = ingredients.save()
                for i in save_objects:
                    self.object.ingredients.add(i)
        return super(RecipeUpdate, self).form_valid(form)

class RecipeDelete(DeleteView):
    model = Recipe
    success_url = reverse_lazy('recipe_list')
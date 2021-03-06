from django.conf import settings
from django.core.cache.backends.base import DEFAULT_TIMEOUT
from django.views.decorators.cache import cache_page
from django.utils.decorators import method_decorator

from django.db.models import Q
from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Ingredient

CACHE_TTL = getattr(settings, 'CACHE_TTL', DEFAULT_TIMEOUT)


@method_decorator(cache_page(CACHE_TTL), name='dispatch')
class IngredientList(ListView):
    model = Ingredient
    paginate_by = 5
    ordering = ["name"]

    def get_queryset(self, *args, **kwargs):
        request = self.request
        query = request.GET.get("q")
        if query:
            return Ingredient.objects.filter(
                Q(article_number__icontains=query) | Q(name__icontains=query)
            )
        return super(IngredientList, self).get_queryset()


class IngredientCreate(CreateView):
    model = Ingredient
    fields = "__all__"
    success_url = reverse_lazy("ingredient_list")


class IngredientUpdate(UpdateView):
    model = Ingredient
    fields = "__all__"
    success_url = reverse_lazy("ingredient_list")


class IngredientDelete(DeleteView):
    model = Ingredient
    success_url = reverse_lazy("ingredient_list")

from django.urls import path

from . import views

urlpatterns = [
    path("", views.IngredientList.as_view(), name="ingredient_list"),
    path("new", views.IngredientCreate.as_view(), name="ingredient_new"),
    path("edit/<int:pk>", views.IngredientUpdate.as_view(), name="ingredient_edit"),
    path("delete/<int:pk>", views.IngredientDelete.as_view(), name="ingredient_delete"),
]

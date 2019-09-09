from django.urls import path

from . import views

urlpatterns = [
    path('', views.RecipeList.as_view(), name='recipe_list'),
    path('new', views.RecipeCreate.as_view(), name='recipe_new'),
    path('detail/<int:pk>', views.RecipeDetail.as_view(), name='recipe_detail'),
    path('edit/<int:pk>', views.RecipeUpdate.as_view(), name='recipe_edit'),
    path('delete/<int:pk>', views.RecipeDelete.as_view(), name='recipe_delete'),
]
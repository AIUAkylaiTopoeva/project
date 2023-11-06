from django.urls import path

from . import views

urlpatterns = [
    path('',views.all_recipes, name="recipe"),
    path('recipe/<str:id>/', views.post_by_id, name="recipe_by_id"),
    path('create/recipe/', views.create_recipe, name="create_recipe"),
    path('update/recipe/<str:id>/', views.update_recipe, name="update_recipe"),
    path('delete/recipe/<str:id>/', views.delete_recipe, name='delete_recipe'),
]
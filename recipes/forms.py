from django import forms
from .models import Recipe, Category

class RecipeForm(forms.ModelForm):
    
    class Meta:
        model = Recipe
        fields = ("__all__")

class CategoryForm(forms.ModelForm):

    class Meta:
        model = Category
        fields = ("__all__")
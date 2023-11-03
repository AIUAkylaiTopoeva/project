from django.http import HttpResponse, HttpRequest
from django.shortcuts import redirect, render
from django.views.decorators.csrf import csrf_exempt
import string

from .models import Recipe, Category
from .forms import CategoryForm, RecipeForm

def all_posts(request:HttpRequest):
    context = {
        'posts':Recipe.objects.all()
    }

    return render(request,'index.html',context=context)

def post_by_id(request, id):
    
    context = {
        'id': id,
        'recipe' : Recipe.objects.get(id=id)
    }
    return render(request,'recipe.html', context=context)


@csrf_exempt
def create_post(request:HttpRequest):
    form = RecipeForm()
    if(request.method == 'POST'):
        form = RecipeForm(data=request.POST)
        form.save()
        return redirect('recipe')

    context = {'form':form,}
    return render(request, "post-form.html", context)

@csrf_exempt
def update_post(request:HttpRequest, id:string):
    recipe = Recipe.objects.get(id=id)
    print(recipe)
    form = RecipeForm(instance=recipe)
    if(request.method == 'POST'):
        form = RecipeForm(data=request.POST, instance=recipe)
        form.save()
        return redirect('recipe')
    
    context = {'form':form,}
    return render(request, "posts-form.html", context)

@csrf_exempt
def delete_post(request, id):
    recipe = Recipe.objects.get(id=id)
    if(request.method == 'POST'):
        recipe.delete()
        return redirect('recipe')
    context = {'recipe':recipe}
    return render(request, 'delete-post.html')

@csrf_exempt
def create_category(request:HttpRequest):
    form = CategoryForm()
    if(request.method == 'POST'):
        form = CategoryForm(data=request.POST)
        form.save()
        return redirect('category')

    context = {'form':form,}
    return render(request, "post-category.html", context)

@csrf_exempt
def delete_category(request, id):
    category = Category.objects.get(id=id)
    if request.method == 'POST':
        category.delete()
        return redirect('category')
    context = {'category':category}
    return render(request, 'category-delete.html')
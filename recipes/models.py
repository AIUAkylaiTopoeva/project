from django.db import models
from slugify import slugify

class Category(models.Model):
    title = models.CharField(max_length=60)
    slug = models.SlugField(blank=True, primary_key=True, max_length=60)

    def __str__(self) -> str:
        return self.title

    def save(self, *args, **kwargs) :
        if not self.slug:
            self.slug = slugify(self.title)
        super().save()

# class Recipe(models.Model):
#     title= models.CharField(max_length=120)
#     body = models.TextField()
#     image = models.ImageField(upload_to='posts/', blank = True)
#     category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='podtd')
#     created_at = models.DateTimeField(auto_now_add=True)
#     uploated_at= models.DateTimeField(auto_now=True)


#     def __str__(self) -> str:
#         return f'{self.title}'
    
# class Comment(models.Model):
#     body = models.TextField()
#     post = models.ForeignKey(Recipe, on_delete=models.CASCADE, related_name='comments')   #related_name является(можем задава$
#     created_at = models.DateTimeField(auto_now_add=True)

#     def __str__(self) -> str:
#         return f'Comment to {self.post.title}'
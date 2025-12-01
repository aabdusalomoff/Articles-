from django.db import models
from django.contrib.auth.models import User


class Category(models.Model):
    name = models.CharField(max_length=200)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name
    

class Article(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    image = models.FileField(upload_to='image')
    category = models.ForeignKey("Category",on_delete=models.CASCADE,related_name='articles')
    author = models.ForeignKey(User,on_delete=models.CASCADE,related_name='articles')
    created_at = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.title


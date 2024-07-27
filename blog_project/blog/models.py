from django.db import models

# 
from django.db import models
from django.contrib.auth.models import User

class Post(models.Model):
    title = models.CharField(max_length=200, verbose_name='Назва')
    content = models.TextField(verbose_name='Зміст')
    published_date = models.DateTimeField(auto_now_add=True, verbose_name='Дата публікації')

    def __str__(self):
        return self.title

class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments', verbose_name='Пост')
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Автор')
    text = models.TextField(verbose_name='Текст')
    created_date = models.DateTimeField(auto_now_add=True, verbose_name='Дата створення')

    def __str__(self):
        return f'Коментар від {self.author} до {self.post}'


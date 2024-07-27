from django.db import models

#___________________________

from django.contrib.auth.models import User

class Task(models.Model):
    STATUS_CHOICES = [
        ('in_progress', 'В процесі...'),
        ('completed', 'Виконано!'),
        ('deferred', 'Відкладено!'),
    ]

    title = models.CharField(max_length=100, verbose_name='Назва')
    description = models.TextField(verbose_name='Опис')
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='in_progress', verbose_name='Статус')
    assigned_to = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Призначений користувач')

    def __str__(self):
        return self.title


# Generated by Django 5.0.7 on 2024-07-27 10:20

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='Назва')),
                ('description', models.TextField(verbose_name='Опис')),
                ('status', models.CharField(choices=[('in_progress', 'В процесі...'), ('completed', 'Виконано!'), ('deferred', 'Відкладено!')], default='in_progress', max_length=20, verbose_name='Статус')),
                ('assigned_to', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Призначений користувач')),
            ],
        ),
    ]

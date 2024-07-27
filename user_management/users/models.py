from django.db import models

#________________
class Role(models.Model):
    ROLE_CHOICES = [
        ('admin', 'Admin'),
        ('user', 'User'),
    ]
    
    name = models.CharField(max_length=30, choices=ROLE_CHOICES, unique=True, verbose_name="Role Name")
    
    def __str__(self):
        return self.name

class User(models.Model):
    name = models.CharField(max_length=255, verbose_name="Full Name")
    email = models.EmailField(unique=True, verbose_name="Email Address")
    role = models.ForeignKey(Role, on_delete=models.CASCADE, verbose_name="Role")
    
    def __str__(self):
        return self.name 

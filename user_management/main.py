from users.models import Role, User

# Створення ролей
admin_role = Role.objects.create(name='admin')
user_role = Role.objects.create(name='user')

# Створення користувачів
user1 = User.objects.create(name="Bread Oiet", email="bread@example.com", role=admin_role)
user2 = User.objects.create(name="Nikole Kate", email="nikole@example.com", role=user_role)

# Перегляд користувачів
print(User.objects.all())

# Зміна ролі користувача
user2.role = admin_role
user2.save()

# Перевірка зміни ролі
print(user2.role.name)
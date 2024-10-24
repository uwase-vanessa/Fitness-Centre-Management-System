from django.db import models
from django.contrib.auth.models import User

# Categories for gym members
CATEGORY = (
    ('Beginner', 'Beginner'),
    ('Intermediate', 'Intermediate'),
    ('Advanced', 'Advanced'),
)


class Customer(models.Model):
    name = models.CharField(max_length=100, null=True, blank=True)
    Hours = models.PositiveIntegerField(null=True, blank=True)
    category = models.CharField(max_length=50, choices=CATEGORY, null=True, blank=True)

    def __str__(self):
        return f'{self.name}-{self.Hours}'

# class Book(models.Model):
#     name = models.ForeignKey(Product, on_delete=models.CASCADE, null=True)
#     client = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
#     Book_quantity = models.PositiveIntegerField(null=True)

#     def __str__(self):
#         return f'{self.client}-{self.name}'

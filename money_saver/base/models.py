from django.db import models
from django.contrib.auth.models import User
from django.utils.timezone import now

# Create your models here.
class Expense(models.Model):
    amount = models.DecimalField(null=True, decimal_places=2, max_digits=25)
    date = models.DateField(default=now)
    description = models.TextField()
    owner = models.ForeignKey(to=User, on_delete=models.CASCADE)
    category = models.CharField(max_length=200)

    def __str__(self):
        return self.category
    
    class Meta:
        ordering: ['-date']
    
class Category(models.Model):
    name=models.CharField(max_length=200)

    class Meta:
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.name

class Income(models.Model):
    amount = models.DecimalField(null=True, decimal_places=2, max_digits=25)
    date = models.DateField(default=now)
    description = models.TextField()
    owner = models.ForeignKey(to=User, on_delete=models.CASCADE)
    category = models.CharField(max_length=200)

    def __str__(self):
        return self.category
    
    class Meta:
        ordering: ['-date']

class IncomeCategory(models.Model):
    name=models.CharField(max_length=200)

    class Meta:
        verbose_name_plural = 'Income Categories'

    def __str__(self):
        return self.name
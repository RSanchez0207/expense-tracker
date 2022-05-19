from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('expenses/', views.expenses, name='expenses'),
    path('income/', views.income, name='income'),
    path('add_wallet/', views.add_wallet, name='add_wallet'),
    path('add_expenses/', views.add_expenses, name='add_expenses'),
    path('edit_expenses/<int:id>', views.edit_expenses, name='edit_expenses'),
    path('delete_expenses/<int:id>', views.delete_expenses, name='delete_expenses'),
    path('add_income/', views.add_income, name='add_income'),
    path('edit_income/<int:id>', views.edit_income, name='edit_income'),
    path('delete_income/<int:id>', views.delete_income, name='delete_income'),
]

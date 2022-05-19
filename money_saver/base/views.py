from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from django.contrib import messages

# Import Models
from .models import Category, Expense, Income, IncomeCategory

# Home Page
@login_required(login_url='/members/login_user')
def home(request):
    expenses = Expense.objects.filter(owner=request.user)
    incomes = Income.objects.filter(owner=request.user)
    context = {
        'expenses': expenses,
        'incomes': incomes
    }
    return render(request, 'base/home.html', context)

# Expenses Page
@login_required(login_url='/members/login_user')
def expenses(request):
    expenses = Expense.objects.filter(owner=request.user)
    context = {
        'expenses': expenses
    }

    return render(request, 'base/expenses.html', context)

# Income Page
@login_required(login_url='/members/login_user')
def income(request):
    incomes = Income.objects.filter(owner=request.user)

    context = {
        'incomes': incomes
    }
    return render(request, 'base/income.html', context)

# Add Wallet Page
@login_required(login_url='/members/login_user')
def add_wallet(request):
    return render(request, 'base/add_wallet.html')

# Add Expense Page
@login_required(login_url='/members/login_user')
def add_expenses(request):
    categories = Category.objects.all()
    context = {'categories': categories,
               'values': request.POST
                }
    if request.method == 'GET':
        return render(request, 'base/add_expenses.html', context)

    if request.method == "POST":
        amount = request.POST['amount']
        expense_date = request.POST['expense_date']
        description = request.POST['description']
        category = request.POST['category']
        if not amount:
            messages.error(request,'Amount not specified.')
            return render(request, 'base/add_expenses.html', context)
        if not expense_date:
            messages.error(request,'Date of expense not specified.')
            return render(request, 'base/add_expenses.html', context)
        
        Expense.objects.create(owner=request.user, amount=amount, date=expense_date, category=category, description=description)
        messages.success(request, 'Transaction saved successfully.')
        return redirect('expenses')

# Edit_Expense Page
@login_required(login_url='/members/login_user')
def edit_expenses(request, id):
    expense = Expense.objects.get(pk=id)
    categories = Category.objects.all()
    context = {
        'expense': expense,
        'values': expense,
        'categories': categories,
    }
    if request.method == 'GET':
        return render(request, 'base/edit_expenses.html', context)
    if request.method == "POST":
        amount = request.POST['amount']
        expense_date = request.POST['expense_date']
        description = request.POST['description']
        category = request.POST['category']
        if not amount:
            messages.error(request,'Amount not specified.')
            return render(request, 'base/edit_expenses.html', context)
        if not expense_date:
            messages.error(request,'Date of expense not specified.')
            return render(request, 'base/edit_expenses.html', context)
        
        expense.owner=request.user 
        expense.amount=amount
        expense.date=expense_date 
        expense.category=category 
        expense.description=description

        expense.save()

        messages.success(request, 'Transaction updated successfully.')
        return redirect('expenses')
    else:
        messages.info(request, 'Handling Post Form')
        return render(request, 'base/edit_expenses.html', context)

# Delete Expense Page
@login_required(login_url='/members/login_user')
def delete_expenses(request, id):
    expense = Expense.objects.get(pk=id)
    expense.delete()
    messages.success(request, 'Transaction Removed.')
    return redirect('expenses')

# Add Income Page
@login_required(login_url='/members/login_user')
def add_income(request):
    categories = IncomeCategory.objects.all()
    context = {'categories': categories,
               'values': request.POST
                }
    if request.method == 'GET':
        return render(request, 'base/add_income.html', context)

    if request.method == "POST":
        amount = request.POST['income_amount']
        income_date = request.POST['income_date']
        description = request.POST['income_description']
        category = request.POST['income_category']
        if not amount:
            messages.error(request,'Amount not specified.')
            return render(request, 'base/income_date.html', context)
        if not income_date:
            messages.error(request,'Date of income not specified.')
            return render(request, 'base/income_date.html', context)
        
        Income.objects.create(owner=request.user, amount=amount, date=income_date, category=category, description=description)
        messages.success(request, 'Income saved successfully.')
        return redirect('income')

# Edit Income Page
@login_required(login_url='/members/login_user')
def edit_income(request, id):
    income = Income.objects.get(pk=id)
    categories = IncomeCategory.objects.all()
    context = {
        'income': income,
        'values': income,
        'categories': categories,
    }
    if request.method == 'GET':
        return render(request, 'base/edit_income.html', context)
    if request.method == "POST":
        amount = request.POST['income_amount']
        income_date = request.POST['income_date']
        description = request.POST['income_description']
        category = request.POST['income_category']
        if not amount:
            messages.error(request,'Amount not specified.')
            return render(request, 'base/edit_income.html', context)
        if not income_date:
            messages.error(request,'Date of income not specified.')
            return render(request, 'base/edit_income.html', context)
        
        income.owner=request.user 
        income.amount=amount
        income.date=income_date 
        income.category=category 
        income.description=description

        income.save()

        messages.success(request, 'Income updated successfully.')
        return redirect('income')
    else:
        messages.info(request, 'Handling Post Form')
        return render(request, 'base/edit_income.html', context)

# Delete Income Page
@login_required(login_url='/members/login_user')
def delete_income(request, id):
    income = Income.objects.get(pk=id)
    income.delete()
    messages.success(request, 'Income Removed.')
    return redirect('income')
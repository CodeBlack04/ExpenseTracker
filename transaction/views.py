from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth.decorators import login_required
from collections import defaultdict

from .models import Transaction, Category
from .forms import NewTransactionForm

# Create your views here.

@login_required
def dashboard(request):
    if request.user.is_authenticated:
        transactions = Transaction.objects.filter(created_by = request.user)
        recent_history = transactions[:5]
    else:
        transactions = None

    if transactions:
        total_income = 0
        total_expense = 0
        total_balance = 0

        income_category_totals = defaultdict(float)
        expense_category_totals = defaultdict(float)

        for transaction in transactions:
            total_balance += transaction.amount

            if transaction.amount > 0:
                total_income += transaction.amount
                income_category_totals[transaction.category] += transaction.amount

            elif transaction.amount < 0:
                total_expense += transaction.amount
                expense_category_totals[transaction.category] += transaction.amount
        
        
        highest_income_category = max(income_category_totals, key=income_category_totals.get, default=None)
        lowest_income_category = min(income_category_totals, key=income_category_totals.get, default=None)

        highest_expense_category = min(expense_category_totals, key=expense_category_totals.get, default=None)
        lowest_expense_category = max(expense_category_totals, key=expense_category_totals.get, default=None)    

    else:
        return redirect('transaction:new')
                
    return render(request, 'transaction/dashboard.html', {
        'recent_history': recent_history,
        'total_income': round(total_income, 2),
        'total_expense': round(total_expense, 2),
        'total_balance': round(total_balance, 2),

        'highest_income_category': highest_income_category,
        'lowest_income_category': lowest_income_category,

        'highest_expense_category': highest_expense_category,
        'lowest_expense_category': lowest_expense_category,

    })

@login_required
def new(request):
    if request.method == 'POST':
        form = NewTransactionForm(request.POST)

        if form.is_valid():
            category = form.cleaned_data['category']
            new_category = form.cleaned_data['new_category']

            if not category and new_category:
                category = Category.objects.create(name=new_category, created_by=request.user)

            Transaction.objects.create(
                category = category,
                name = form.cleaned_data['name'],
                notes = form.cleaned_data['notes'],
                amount = form.cleaned_data['amount'],
                created_by = request.user
            )
            return redirect('transaction:dashboard')
    else:
        form = NewTransactionForm()

    return render(request, 'transaction/form.html', { 'form': form })

@login_required
def list(request):
    transactions = Transaction.objects.filter(created_by=request.user)
    return render(request, 'transaction/list.html', {
        'transactions': transactions,
    })

@login_required
def incomes(request):
    incomes = Transaction.objects.filter(created_by=request.user).filter(amount__gt=0)
    return render(request, 'transaction/incomes.html', {
        'incomes': incomes,
    })

@login_required
def expenses(request):
    expenses = Transaction.objects.filter(created_by=request.user).filter(amount__lt=0)
    return render(request, 'transaction/expenses.html', {
        'expenses': expenses,
    })
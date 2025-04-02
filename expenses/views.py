import os
import csv
from django.shortcuts import render, redirect
from django.conf import settings
from .models import UserProfile, Expense
from .forms import (
    EntranceForm,
    ExistingUserLoginForm,
    NewUserRegistrationForm,
    ExpenseForm,
)

def entrance_view(request):
    if request.method == 'POST':
        form = EntranceForm(request.POST)
        if form.is_valid():
            code = form.cleaned_data['code']
            if code == "1926":
                return redirect('login_register')
            else:
                form.add_error('code', 'Incorrect code')
    else:
        form = EntranceForm()
    return render(request, 'expenses/entrance.html', {'form': form})

def login_register_view(request):
    login_form = ExistingUserLoginForm()
    register_form = NewUserRegistrationForm()
    
    if request.method == 'POST':
        # Determine which form was submitted by checking the button name.
        if 'login' in request.POST:
            login_form = ExistingUserLoginForm(request.POST)
            if login_form.is_valid():
                name = login_form.cleaned_data['name']
                pin = login_form.cleaned_data['pin']
                try:
                    user = UserProfile.objects.get(name=name)
                    if user.pin == pin:
                        request.session['user_id'] = user.id
                        return redirect('add_expense')
                    else:
                        login_form.add_error('pin', 'Invalid PIN')
                except UserProfile.DoesNotExist:
                    login_form.add_error('name', 'User does not exist')
                    
        elif 'register' in request.POST:
            register_form = NewUserRegistrationForm(request.POST)
            if register_form.is_valid():
                name = register_form.cleaned_data['name']
                pin = register_form.cleaned_data['pin']
                confirm_pin = register_form.cleaned_data['confirm_pin']
                
                if pin != confirm_pin:
                    register_form.add_error('confirm_pin', "PINs do not match")
                else:
                    # Check if a user with the given name already exists
                    if UserProfile.objects.filter(name=name).exists():
                        register_form.add_error('name', 'User with this name already exists. Please login instead.')
                    else:
                        # Create a new user and store in DB.
                        user = UserProfile.objects.create(name=name, pin=pin)
                        request.session['user_id'] = user.id
                        
                        # Save registration data to CSV.
                        csv_file = os.path.join(settings.BASE_DIR, 'data', 'users.csv')
                        os.makedirs(os.path.dirname(csv_file), exist_ok=True)
                        with open(csv_file, 'a', newline='') as f:
                            writer = csv.writer(f)
                            writer.writerow([user.id, name, pin])
                            
                        return redirect('add_expense')
                        
    return render(request, 'expenses/login_register.html', {
        'login_form': login_form,
        'register_form': register_form
    })
def add_expense(request):
    user_id = request.session.get('user_id')
    if not user_id:
        return redirect('login_register')
    user = UserProfile.objects.get(id=user_id)

    if request.method == 'POST':
        form = ExpenseForm(request.POST)
        if form.is_valid():
            expense = form.save(commit=False)
            expense.user_id = user_id
            expense.save()
            # Save expense data to CSV.
            csv_file = os.path.join(settings.BASE_DIR, 'data', 'expenses.csv')
            os.makedirs(os.path.dirname(csv_file), exist_ok=True)
            with open(csv_file, 'a', newline='') as f:
                writer = csv.writer(f)
                writer.writerow([
                    expense.id,
                    user_id,
                    user.name,
                    expense.location,
                    expense.product,
                    expense.price,
                    expense.quantity,
                    expense.date,
                ])
            return redirect('add_expense')
    else:
        # Pre-fill location if there's an existing expense for this user.
        initial = {}
        last_expense = Expense.objects.filter(user_id=user_id).order_by('-date').first()
        if last_expense:
            initial['location'] = last_expense.location
        form = ExpenseForm(initial=initial)
    
    expenses = Expense.objects.filter(user_id=user_id)
    return render(request, 'expenses/add_expense.html', {'form': form, 'expenses': expenses})
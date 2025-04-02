from django import forms
from .models import Expense

class EntranceForm(forms.Form):
    code = forms.CharField(max_length=10, label="Enter Entrance Code")

class ExistingUserLoginForm(forms.Form):
    name = forms.CharField(max_length=100)
    pin = forms.CharField(max_length=6, widget=forms.PasswordInput)

class NewUserRegistrationForm(forms.Form):
    name = forms.CharField(max_length=100)
    pin = forms.CharField(max_length=6, widget=forms.PasswordInput)
    confirm_pin = forms.CharField(max_length=6, widget=forms.PasswordInput)

class ExpenseForm(forms.ModelForm):
    class Meta:
        model = Expense
        fields = ['location', 'product', 'price','quantity']
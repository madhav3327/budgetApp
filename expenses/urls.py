from django.urls import path
from .views import entrance_view, login_register_view, add_expense

urlpatterns = [
    path('', entrance_view, name='entrance'),
    path('login_register/', login_register_view, name='login_register'),
    path('expense/', add_expense, name='add_expense'),
]
# accounts/views.py
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from .forms import RegisterForm, LoginForm, EmployeeUpdateForm
from .models import CustomUser

def register_view(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = RegisterForm()
    return render(request, 'accounts/register.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request, data=request.POST)
        if form.is_valid():
            login(request, form.get_user())
            return redirect('dashboard')
    else:
        form = LoginForm()
    return render(request, 'accounts/login.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('login')

@login_required
def dashboard(request):
    employees = CustomUser.objects.all()
    return render(request, 'accounts/dashboard.html', {'employees': employees})

@login_required
def update_employee(request, pk):
    employee = get_object_or_404(CustomUser, pk=pk)
    if request.method == 'POST':
        form = EmployeeUpdateForm(request.POST, instance=employee)
        if form.is_valid():
            form.save()
            return redirect('dashboard')
    else:
        form = EmployeeUpdateForm(instance=employee)
    return render(request, 'accounts/update_employee.html', {'form': form})

@login_required
def delete_employee(request, pk):
    employee = get_object_or_404(CustomUser, pk=pk)
    if request.method == 'POST':
        employee.delete()
        return redirect('dashboard')
    return render(request, 'accounts/delete_employee.html', {'employee': employee})

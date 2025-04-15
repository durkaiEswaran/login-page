# from django.shortcuts import render, redirect, get_object_or_404
# from .models import User
# from .forms import UserForm
# def login(requesrt):
#     pass
# def user_list(request):
#     users = User.objects.all()
#     return render(request, 'accounts/user_list.html', {'users': users})

# def user_create(request):
#     if request.method == 'POST':
#         form = UserForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('user_list')
#     else:
#         form = UserForm()
#     return render(request, 'accounts/user_form.html', {'form': form})

# def user_update(request, pk):
#     user = get_object_or_404(User, pk=pk)
#     if request.method == 'POST':
#         form = UserForm(request.POST, instance=user)
#         if form.is_valid():
#             form.save()
#             return redirect('user_list')
#     else:
#         form = UserForm(instance=user)
#     return render(request, 'accounts/user_form.html', {'form': form})

# def user_delete(request, pk):
#     user = get_object_or_404(User, pk=pk)
#     if request.method == 'POST':
#         user.delete()
#         return redirect('user_list')
#     return render(request, 'accounts/user_confirm_delete.html', {'user': user})
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required, user_passes_test
from .models import User
from django.views.decorators.http import require_http_methods
from django.views.decorators.csrf import csrf_exempt
import json

# Login View
def login_view(request):
    if request.method == 'POST':
        import json
        data = json.loads(request.body)
        username = data.get('username')
        password = data.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None and user.is_superuser:
            login(request, user)
            return JsonResponse({'success': True}, status=200)
        return JsonResponse({'success': False, 'message': 'Invalid credentials or not superuser'}, status=401)

    return render(request, 'accounts/login.html')

# Logout (optional)
def logout_view(request):
    logout(request)
    return redirect('login')

@login_required
def dashboard(request):
    return render(request, 'accounts/dashboard.html')

@login_required
def user_list_api(request):
    return render(request, 'accounts/user_list.html')
@csrf_exempt
def user_create_api(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        user = User.objects.create(**data)
        return JsonResponse({'message': 'User created', 'user_id': user.id}, status=201)

@csrf_exempt
def user_update_api(request, pk):
    try:
        user = User.objects.get(pk=pk)
    except User.DoesNotExist:
        return JsonResponse({'error': 'User not found'}, status=404)

    if request.method == 'PUT':
        data = json.loads(request.body)
        for field, value in data.items():
            setattr(user, field, value)
        user.save()
        return JsonResponse({'message': 'User updated'})

@csrf_exempt
def user_delete_api(request, pk):
    try:
        user = User.objects.get(pk=pk)
        user.delete()
        return JsonResponse({'message': 'User deleted'})
    except User.DoesNotExist:
        return JsonResponse({'error': 'User not found'}, status=404)
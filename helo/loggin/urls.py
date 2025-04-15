from django.urls import path
from . import views

urlpatterns = [
    path('', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('dashboard/', views.dashboard, name='dashboard'),  # Add this if not already
    path('api/users/', views.user_list_api, name='user_list_api'),
    path('api/users/create/', views.user_create_api, name='user_create_api'),
    path('api/users/update/<int:pk>/', views.user_update_api, name='user_update_api'),
    path('api/users/delete/<int:pk>/', views.user_delete_api, name='user_delete_api'),
]


    # path('create/', views.user_create, name='user_create'),
    # path('update/<int:pk>/', views.user_update, name='user_update'),
    # path('delete/<int:pk>/', views.user_delete, name='user_delete'),


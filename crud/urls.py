from django.urls import path
from . import views

app_name = 'crud'

urlpatterns = [
    path('', views.task_list_and_create, name='task_list'),
    path('update/<int:pk>/', views.task_update, name='task_update'),
    path('edit/<int:pk>/', views.task_edit, name='task_edit'),
    path('delete/<int:pk>/', views.task_delete, name='task_delete'),
]
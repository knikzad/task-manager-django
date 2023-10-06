from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('login_user', views.login_user, name='login'),
    path('logout_user', views.logout_user, name='logout'),
    path('register_user', views.register_user, name='register'),
  
    path('tasks/ajax/', views.task_ajax, name='task-ajax'),
  
    path('tasks/<int:pk>/', views.task_detail, name='task-detail'),
  
    path('tasks/update/<int:pk>/', views.update_task, name='update-task'),
    path('tasks/update_status/<int:pk>/', views.update_task_status, name='update-task-status'),
  
    path('tasks/delete/<int:pk>/', views.delete_task, name='delete-task'),
  
    path('tasks/add/', views.add_task, name='add-task'),
]

from django.urls import path
from . import views
from .views import TaskList, TaskDetails, TaskCreate, TaskUpdate, TaskDelete, customLoginView
from django.contrib.auth.views import LogoutView
from rest_framework_simplejwt.views import TokenRefreshView





urlpatterns = [
    path('api/login/', customLoginView.as_view(), name = 'login'),
    path('logout/', LogoutView.as_view(next_page='login'), name = 'logout'),
    path('', TaskList.as_view(), name = 'tasks'),
    path('task/<int:pk>/', TaskDetails.as_view(), name ='task'),
    path('task-create/', TaskCreate.as_view(), name = 'task-create'),
    path('task-update/<int:pk>/', TaskUpdate.as_view(), name = 'task-update'),
    path('task-delete/<int:pk>/', TaskDelete.as_view(), name = 'task-delete'),
]
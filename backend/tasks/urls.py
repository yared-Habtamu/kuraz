from django.urls import path
from .views import TaskList, TaskDetail, HomeView

urlpatterns = [
    path('api/tasks/', TaskList.as_view(), name='task-list'),
    path('api/tasks/<int:pk>/', TaskDetail.as_view(), name='task-detail'),
    path('', HomeView.as_view(), name='home'),
]
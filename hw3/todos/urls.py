from django.urls import path
from . import views

urlpatterns = [
    path('', views.get_todos, name='get_todos'),
    path('<int:id>/', views.view_todo, name='view_todo'),
    path('<int:id>/delete/', views.delete_todo, name='delete_todo'),
]

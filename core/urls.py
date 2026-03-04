from django.urls import path

from . import views

app_name = 'core'

urlpatterns = [
    path('', views.home, name='home'),
    path('api/todos/', views.todos, name='todos'),
    path('api/todos/<int:todo_id>/toggle/', views.toggle_todo, name='toggle'),
]

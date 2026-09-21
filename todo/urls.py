from django.urls import path
from . import views

app_name = 'todo'

urlpatterns = [
    path('', views.todo, name = "todo"),
    path('insert/', views.todoInsert, name = "todo"),
    path('update/', views.todoUpdate, name = "todoUpdate"),
    path('delete/', views.todoDelete, name = "todoDelete"),
    path('complete/', views.todoComplete, name='todoComplete'),
]
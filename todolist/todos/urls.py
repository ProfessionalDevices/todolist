from django.conf.urls import url
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('todos/details/<int:pk>', views.details, name='details'),
    path('add', views.add, name='add'),
    path('details/<int:pk>/todo-delete', views.TodoDelete.as_view(), name = 'delete_todo'),
    path('details/<int:pk>/todo-update', views.TodoUpdate.as_view(), name = 'update_todo'),
]

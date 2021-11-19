from django.urls import path
from . import views

urlpatterns = {
    path('index', views.view_todos, name='index'),
    path('update', views.update_todo, name='update'),
    path('delete', views.delete_todo, name='delete')
}
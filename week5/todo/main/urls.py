from django.urls import path
from . import views

app_name = 'main'
urlpatterns = [
	path('', views.index, name = 'index'),
	path('completed/', views.completed, name = 'completed'),
	path('add/', views.add, name = 'add'),
	path('delete/<int:task_id>', views.delete, name = 'delete'),
	path('change/<int:task_id>', views.change, name = 'change'),
]

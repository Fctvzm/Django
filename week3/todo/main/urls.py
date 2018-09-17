from django.urls import path
from . import views

app_name = 'main'
urlpatterns = [
	path('', views.index, name = 'index'),
	path('<int:task_id>/', views.detail, name = 'detail'),
	path('completed/', views.completed, name = 'completed'),
]

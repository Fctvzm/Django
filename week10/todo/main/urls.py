from django.urls import path
from . import views

app_name = 'main'
urlpatterns = [
	path('', views.IndexView.as_view(), name = 'index'),
	path('completed/', views.CompletedListView.as_view(), name = 'completed'),
	path('add/', views.TaskCreateView.as_view(), name = 'add'),
	path('delete/<int:pk>', views.TaskDeleteView.as_view(), name = 'delete'),
	path('change/<int:pk>', views.TaskUpdateView.as_view(), name = 'change'),
]

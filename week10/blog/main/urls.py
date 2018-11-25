from django.urls import path
from . import views


urlpatterns = [
	path('', views.IndexView.as_view(), name = 'index'),
	path('<int:pk>/', views.PostDetailView.as_view(), name = 'detail'),
	path('addPost/', views.PostCreateView.as_view(), name = 'addPost'),
	path('<int:pk>/addComment/', views.CommentCreateView.as_view(), name = 'addComment'),
]
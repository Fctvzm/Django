from api import views
from django.urls import path

urlpatterns = [
    path('posts/', views.post_list),
    path('posts/<int:pk>/', views.post_detail),
    path('posts/<int:pk>/comment', views.comment),
]
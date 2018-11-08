from django.urls import path
from . import views

urlpatterns = [
	path('', views.IndexView.as_view(), name = 'index'),
	path('<int:pk>/', views.ResDetailView.as_view(), name = 'res_detail'),
	path('res_add/', views.ResCreateView.as_view(), name = 'res_add'),
	path('<int:pk>/res_delete/', views.ResDeleteView.as_view(), name = 'res_delete'),
	path('<int:pk>/res_change/', views.ResUpdateView.as_view(), name = 'res_change'),
	#path('<int:res_id>/addReview/', views.res_review, name = 'res_review'),
	#path('dishes/<int:dish_id>/addReview/', views.dish_review, name = 'dish_review'),
	path('dishes/', views.DishView.as_view(), name = 'dishes'),
	#path('dishes/<int:dish_id>/', views.dish_detail, name = 'dish_detail'),
]
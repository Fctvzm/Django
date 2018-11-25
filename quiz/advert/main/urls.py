from django.urls import path
from main import views, CBV
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    path('login/',views.login),
    
    path('adverts/', views.advert_list),
    path('adverts/<int:pk>/', views.advert_detail),

   	#('adverts/', CBV.AdvertList.as_view()),
    #path('adverts/<int:pk>/', CBV.AdvertDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
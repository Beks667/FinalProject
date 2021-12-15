from django.urls import path,include
from serials import views
from rest_framework.urlpatterns import format_suffix_patterns


urlpatterns = [
   
    path('product/',views.ProductListView.as_view()),
    path('product/<int:pk>/',views.ProductDetailView.as_view()),
    path('category/',views.CategoryListView.as_view()),
    path('category/<int:pk>/',views.CategoryDetailView.as_view()),
    
]


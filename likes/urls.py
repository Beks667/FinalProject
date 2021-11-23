from django.urls import path
from .views import *

urlpatterns=[
    path('likes/<int:pk>/',LikeListCreate.as_view()),
    

    ]
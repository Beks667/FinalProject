from django.urls import path
from .views import *

urlpatterns=[
    path('likes/',LikeListCreate.as_view()),
    

    ]
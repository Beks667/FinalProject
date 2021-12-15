from django.urls import path
from .views import *

urlpatterns=[
    path('comments/',CommentListView.as_view()),
    path('comments/<int:pk>/',CommentDetailView.as_view())

    ]
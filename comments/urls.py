from django.urls import path
from .views import *

urlpatterns=[
    path('comments/',CommentListView.as_view()),
    path('detail/',CommentDetailView.as_view())

    ]
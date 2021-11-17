from django.urls import path
from accounts.views import RegistrationAPIView,LoginAPIView,LogoutAPIView,GetUserAPIView


urlpatterns=[
    path('register/',RegistrationAPIView.as_view()),
    path('login/', LoginAPIView.as_view()),
    path('logout/', LogoutAPIView.as_view()),
    path('user/', GetUserAPIView.as_view()),
]
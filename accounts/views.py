from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from accounts.serializers import RegistrationSerializer,LoginSerializer,UserSerializer
from django.contrib.auth import get_user_model

from rest_framework.authtoken.models import Token
from drf_yasg.utils import swagger_auto_schema
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth import authenticate

User=get_user_model()

class RegistrationAPIView(APIView):

    @swagger_auto_schema(operations_description='Upload thumbnail',
                        request_body=RegistrationSerializer, )
    def post(self,request):
        serializer =RegistrationSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        username= serializer.validated_data.get('username')
        password = serializer.validated_data.get('password')

        if User.objects.filter(username=username).exists():
            return Response({'message:User with such username already exists'},
                            status=status.HTTP_400_BAD_REQUEST)

        user = User.objects.create_user(username=username,password = password)
        token= Token.objects.create(user=user)

        return Response({'token':token.key})

class LoginAPIView(APIView):
    
    def get(self, request):
        serializer = LoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        username =serializer.validated_data.get('username')
        password =serializer.validated_data.get('password')
        user = authenticate(username=username, password=password)

        if user is not None:
            token, _ = Token.objects.get_or_create(user=user)
            return Response({'token': token.key,}, status=status.HTTP_200_OK)
        return Response({'message': 'Не валидные данные'},
                         status=status.HTTP_400_BAD_REQUEST)

class LogoutAPIView(APIView):
    permission_classes=[IsAuthenticated, ]

    def post(self, request):
        user = request.user
        token = Token.objects.filter(user=user).first()
        token.delete()
        return Response({'message': 'True'})

class GetUserAPIView(APIView):
    permission_classes=[IsAuthenticated, ]

    def get(self, request):
        user = request.user
        serializers = UserSerializer(user, many=False)
        return Response(serializers.data)
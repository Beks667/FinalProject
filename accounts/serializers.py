from django.core import exceptions
from rest_framework import serializers
from django.contrib.auth.models import User



class RegistrationSerializer(serializers.Serializer):
    username =serializers.CharField()
    password = serializers.CharField()
    password2 = serializers.CharField()

    def validate(self, data):
        data = super().validate(data)
        if data.get('password') != data.get('password2'):
            raise exceptions.ValidationError('Password do not match')
        return data

    # def validate_password(self,value):
    #     if len(value)<5:
    #         return exceptions.ValidationError('passw too short')
    #     elif len(value)>20:
    #         return exceptions.ValidationError('passw is too long')
    #     else:
    #         return value

class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username']

    
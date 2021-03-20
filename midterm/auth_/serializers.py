from rest_framework import serializers

from auth_.models import MainUser


class LoginSerializer(serializers.Serializer):
    email = serializers.CharField()
    password = serializers.CharField()

class RegisterSerializer(serializers.Serializer):
    email = serializers.CharField()
    password = serializers.CharField()

    def save(self):
        MainUser.objects.create_user(self.validated_data['email'],
                                     self.validated_data['password'])
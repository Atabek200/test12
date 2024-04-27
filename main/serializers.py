from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainSerializer
from .models import CarBrand


class CarBrandSerializer(serializers.ListSerializer):

    class Meta:
        model = CarBrand
        fields = '__all__'


class MyTokenObtainSerializer(TokenObtainSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        token['custom_field'] = user.custom_field
        return token

    def validate(self, attrs):
        data = super().validate(attrs)
        return data
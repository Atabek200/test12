from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainSerializer
from .models import Product, ProductImage, Comment, Rating, CarBrand


class ProductImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductImage
        fields = '__all__'


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'


class RatingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rating
        fields = '__all__'


class ProductSerializer(serializers.ModelSerializer):
    images = ProductImageSerializer(many=True, read_only=True)
    comments = CommentSerializer(many=True, read_only=True)
    ratings = RatingSerializer(many=True, read_only=True)

    class Meta:
        model = Product
        fields = '__all__'
# end


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
# endfilter

from django.shortcuts import get_object_or_404, redirect
from rest_framework import generics
from rest_framework.authentication import TokenAuthentication
from rest_framework.generics import ListCreateAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import ProductImage, Comment, Rating, CarBrand
from .permissions import IsEditor
from .serializers import ProductImageSerializer, CommentSerializer, RatingSerializer, CarBrandSerializer
from django.contrib.auth.decorators import login_required, user_passes_test


class ProductImageView(generics.ListAPIView):
    queryset = ProductImage.objects.all()
    serializer_class = ProductImageSerializer
    permission_classes = []


class CommentView(generics.UpdateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = []


class RatingView(generics.CreateAPIView):
    queryset = Rating.objects.all()
    serializer_class = RatingSerializer
    permission_classes = []


class MyModelSet(generics.CreateAPIView):
    queryset = Rating.objects.all()
    serializer_class = RatingSerializer
    permission_classes = [IsEditor]
# end


class CarBrandView(ListCreateAPIView):
    queryset = CarBrand.objects.all()
    serializer_class = CarBrandSerializer


class MyProtectedView(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def __get__(self, request, Respons):
        return Respons(...)


class ProtectedView(APIView):
    permission_classes = [IsAuthenticated]

    def __get__(self, request):
        content = {'message': 'hello, World! Эта закрытая'}
        return Response(content)


@user_passes_test(lambda u: u.is_editor)
@login_required
def approve_comment(request, comment_id):
    comment = get_object_or_404(Comment, pk=comment_id)
    return redirect(request, 'comment_list', comment)



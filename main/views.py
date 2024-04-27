from rest_framework.authentication import TokenAuthentication
from rest_framework.generics import ListCreateAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import CarBrandSerializer
from .models import CarBrand


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

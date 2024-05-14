from django.shortcuts import render
from rest_framework.authentication import TokenAuthentication
from rest_framework.generics import ListCreateAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import CarBrandSerializer
from .models import CarBrand


def index(request):
    return render(request, 'index.html')


def Appointmentofthemaster(request):
    return render(request, 'Administrative functionality.html')


def Workprogresstracking(request):
    return render(request, 'Appointment of the master.html')


def Notifications(request):
    return render(request, 'Notifications.html')


def Administrativefunctionality(request):
    return render(request, 'Work progress tracking.html')


def interface(request):
    return render(request, 'interface.html')


def Safety(request):
    return render(request, 'Safety.html')


def Performance(request):
    return render(request, 'Performance.html')


def Scalability(request):
    return render(request, 'Scalability.html')


def Technologystack(request):
    return render(request, 'Technology stack.html')


def Workplan(request):
    return render(request, 'Work plan.html')


def Expectedresults(request):
    return render(request, 'Expected results.html')


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

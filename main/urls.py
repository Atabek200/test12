from django.urls import path
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from . import views

name = DefaultRouter()
name.register(r'main.urls', views.CarBrandView)

urlpatterns = [
   path('', views.CarBrandView.as_view()),
   path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
   path('api/token/refresh/', TokenRefreshView.as_view(), name='token_obtain_pair'),
]

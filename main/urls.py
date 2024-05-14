from django.urls import path
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from . import views

name = DefaultRouter()
name.register(r'main.urls', views.CarBrandView)

urlpatterns = [
   path('', views.CarBrandView.as_view()),
   path('articles/', views.index, name='home'),
   path('masters/', views.Appointmentofthemaster, name='masters'),
   path('tracking/', views.Workprogresstracking, name='tracking'),
   path('notifications/', views.Notifications, name='notifications'),
   path('administrative/', views.Administrativefunctionality, name='administrative'),
   path('interface/', views.interface, name='interface'),
   path('safety/', views.Safety, name='safety'),
   path('performance/', views.Performance, name='performance'),
   path('scalability', views.Scalability, name='scalability'),
   path('technology_stack/', views.Technologystack, name='technology_stack'),
   path('work_plan/', views.Workplan, name='work_plan'),
   path('expected_results', views.Expectedresults, name='expected_results'),
   path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
   path('api/token/refresh/', TokenRefreshView.as_view(), name='token_obtain_pair'),
]

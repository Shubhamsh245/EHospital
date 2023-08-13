
from django.urls import path,include
from . import views

urlpatterns = [
    path('', views.homePage, name="homePage"),
    path('about/', views.aboutPage, name="aboutPage"),
    path('emergency/', views.formPage, name="emergencyPage"),
    path('hospitals/', views.hospitalsPage, name="hospitalsPage"),
    path('registration/', views.registrationPage, name="registrationPage"),
    path('hospitals/dashboard/<str:name>', views.dashboard, name="dashboard"),
    path('logout/',views.logoutPage, name="logout"),
    path('form/',views.formPage, name="formPage"),
]

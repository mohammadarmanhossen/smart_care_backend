from rest_framework.routers import DefaultRouter
from django.urls import path, include
from rest_framework import routers
from .import views

routers=routers.DefaultRouter() #wifi router toiriy korlam
routers.register('',views.AppointmentViewSet) # akta antena toiriy korlam

urlpatterns = [
    path('',include(routers.urls)),
]

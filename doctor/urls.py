from rest_framework.routers import DefaultRouter
from django.urls import path, include
from .import views

router = DefaultRouter() # amader router
router.register('list', views.DoctorViewset)
router.register('specialization', views.SpecializationViewset) 
router.register('designation', views.DesignationViewset) 
router.register('available_time', views.AvailableTimeViewset) 
router.register('review', views.ReviewTimeViewset) 

 # router er antena
urlpatterns = [
    path('', include(router.urls)),
]
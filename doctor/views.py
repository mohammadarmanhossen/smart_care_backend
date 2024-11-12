from django.shortcuts import render
from rest_framework import viewsets
from .import serializer
from .import models
from rest_framework import filters,pagination
class DoctorPagination(pagination.PageNumberPagination):
    page_size=1  # item per page
    page_size_query_param = 'page_size'
    max_page_size = 100

class DoctorViewset(viewsets.ModelViewSet):
    queryset = models.Doctor.objects.all()
    serializer_class = serializer.DoctorSerializer
    filter_backends=[filters.SearchFilter]
    pagination_class=DoctorPagination
    search_fields=['user_first_name','user_email','designation_name','specialization_name']

class AvailableTimeForSpecificDoctor(filters.BaseFilterBackend):
    def filter_queryset(self, request, queryset, view):
        doctor_id=request.query_params.get('doctor_id')
        if doctor_id:
            return queryset.filter(doctor=doctor_id)

    #def get_queryset(self):
    #     queryset=super().get_queryset()
    #     doctor_id=self.request.query_params.get('doctor_id')
    #     if doctor_id:
    #         queryset=queryset.filter(doctor_id=doctor_id)
    #     return queryset

class SpecializationViewset(viewsets.ModelViewSet):
    queryset = models.Specialization.objects.all()
    serializer_class = serializer.SpecializationSerializer

class DesignationViewset(viewsets.ModelViewSet):
    queryset = models.Designation.objects.all()
    serializer_class = serializer.DesignationSerializer

class AvailableTimeViewset(viewsets.ModelViewSet):
    queryset = models.AvailableTime.objects.all()
    serializer_class = serializer.AvailableTimeSerializer
    filter_backends=[AvailableTimeForSpecificDoctor]

class ReviewTimeViewset(viewsets.ModelViewSet):
    queryset = models.Review.objects.all()
    serializer_class = serializer.ReviewSerializer


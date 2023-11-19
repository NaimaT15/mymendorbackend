from django.urls import path
from django.urls import re_path

from .views import Service_list, Requirment_list,Record_Service,Requirment_record,UpdateServiceViewSet
urlpatterns = [
     path('service_list/',Service_list.as_view(),name="service_list"),
     path('record_service/',Record_Service.as_view(),name="Record_Service"),
     path('requirment_list/',Requirment_list.as_view()),
     path('requirment_record/',Requirment_record.as_view()),
     path('update/<int:pk>/',UpdateServiceViewSet.as_view()),
    ]

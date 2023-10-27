from django.urls import path
from .views import Service_list, Requirment_list
urlpatterns = [
     path('service_list/',Service_list.as_view()),
     path('requirment_list/',Requirment_list.as_view()),
]

from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import render
from django.http import Http404
from rest_framework.views import APIView
from .models import services,general_requirment
from .serializers import ServiceSerializer,RequirmentSerializer

class Service_list(APIView):
    serializer_class=ServiceSerializer
    
    def get(self, request, format=None):
        service = services.objects.all()
        serializer = ServiceSerializer(service, many=True)
        return Response(serializer.data)
  
    def post(self, request, format=None):
        serializer = ServiceSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,
                            status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class Requirment_list(APIView):
    serializer_class=RequirmentSerializer
    
    def get(self, request, format=None):
        requirments = general_requirment.objects.all()
        serializer = RequirmentSerializer( requirments, many=True)
        return Response(serializer.data)
  
    def post(self, request, format=None):
        serializer = RequirmentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,
                            status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
  






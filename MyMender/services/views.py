from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import render
from django.http import Http404
from rest_framework.views import APIView
from .models import services,general_requirment
from .serializers import ServiceSerializer,RequirmentSerializer,UpdateServiceSerializer
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated, AllowAny
class Service_list(APIView):
    serializer_class=ServiceSerializer
    
    def get(self, request, format=None):
        service = services.objects.all()
        serializer = ServiceSerializer(service, many=True)
        return Response(serializer.data)

class Record_Service(APIView):
    serializer_class=ServiceSerializer

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
    
class Requirment_record(APIView):
    serializer_class=RequirmentSerializer
    def post(self, request, format=None):
        serializer = RequirmentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,
                            status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
  


class AddService(generics.GenericAPIView):
    serializer_class = ServiceSerializer
    queryset = services.objects.all()
    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"status": "success", "Feedback": serializer.data}, status=status.HTTP_201_CREATED)
        else:
            return Response({"status": "fail", "message": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)


class UpdateServiceViewSet(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ServiceSerializer
    queryset = services.objects.all()
    
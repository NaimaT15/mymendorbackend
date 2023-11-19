from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import render
from django.http import Http404
from rest_framework.views import APIView
from .models import announcement
from .serializers import announceSerializer

class announce(APIView):
    serializer_class=announceSerializer
  
    def post(self, request, format=None):
        serializer = announceSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,
                            status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

class announce_list(APIView):
    serializer_class=announceSerializer
    
    def get(self, request, format=None):
        announce = announcement.objects.all()
        serializer = announceSerializer(announce, many=True)
        return Response(serializer.data)
  



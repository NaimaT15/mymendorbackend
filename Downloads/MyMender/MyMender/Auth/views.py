from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import render
from django.http import Http404
from rest_framework.views import APIView
from .models import User, admin, department
from .serializers import UserSerializer, AdminSerializer, departmentSerializer

class user_list(APIView):
    serializer_class=UserSerializer
    
    def get(self, request, format=None):
        account =User.objects.all()
        serializer = UserSerializer(account, many=True)
        return Response(serializer.data)
  
    def post(self, request, format=None):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,
                            status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class admin_list(APIView):
    serializer_class=AdminSerializer
    
    def get(self, request, format=None):
        admins =admin.objects.all()
        serializer = AdminSerializer(admins, many=True)
        return Response(serializer.data)
  
    def post(self, request, format=None):
        serializer = AdminSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,
                            status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class dep(APIView):
    serializer_class=departmentSerializer
    
    def get(self, request, format=None):
        dept = department.objects.all()
        serializer = departmentSerializer(dept, many=True)
        return Response(serializer.data)
  
    def post(self, request, format=None):
        serializer = departmentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,
                            status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
  
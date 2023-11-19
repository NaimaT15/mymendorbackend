import json
from rest_framework.response import Response

from django.shortcuts import render, redirect
from django.forms import ValidationError
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.decorators import api_view
from pyexpat.errors import messages
#from rest_auth.views import LoginView as RestLoginView
from rest_framework.authtoken.serializers import AuthTokenSerializer
from knox.auth import AuthToken, TokenAuthentication
from rest_framework import status
from django.shortcuts import render
from django.http import Http404, HttpResponse
from django.contrib.auth import authenticate,login,logout
from rest_framework.views import APIView
from .models import User, admin, department
from MymenderProject.decorators import admin_only, customer_required, superuser_required
from .serializers import RegisteradminSerializer, UserLoginSerializer, UserLogoutSerializer, UserSerializer, AdminSerializer, departmentSerializer,RegistrationSerializer
from services import urls as url
from appointment import models as appo
from rest_framework import viewsets
from rest_framework.authentication import SessionAuthentication
from rest_framework.permissions import IsAuthenticated, AllowAny, IsAdminUser



class user_list(APIView):
    serializer_class=UserSerializer
    authentication_classes=[SessionAuthentication]
    permission_classes=[IsAdminUser] 
    
    def get(self, request, format=None):
        account =User.objects.filter(is_customer=True).all()
        serializer = UserSerializer(account, many=True)
        return Response(serializer.data)

class dep_list(APIView):
    serializer_class=departmentSerializer
    # authentication_classes=[SessionAuthentication]
    # permission_classes=[IsAuthenticated] 
    
    def get(self, request, format=None):
        account =department.objects.all()
        serializer = departmentSerializer(account, many=True)
        return Response(serializer.data)
 
class register_user(APIView):
    serializer_class=RegistrationSerializer
    # authentication_classes=[SessionAuthentication]

    # permission_classes=[AllowAny] 

    def get(self, request, format=None):
        account =User.objects.all()
        serializer = UserSerializer(account, many=True)
        return Response(serializer.data)
    
    def post(self, request, format=None):
        serializer = RegistrationSerializer(data=request.data)
        if serializer.is_valid():
            
            serializer.save()
            return Response(serializer.data,
                            status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class register_admin(APIView):
    serializer_class=RegisteradminSerializer
    authentication_classes=[SessionAuthentication]
    permission_classes=[AllowAny]     
    
    def post(self, request, format=None):
        serializer = RegisteradminSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,
                            status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class admin_list(APIView):
    serializer_class=UserSerializer
    authentication_classes=[SessionAuthentication]

    permission_classes=[AllowAny] 
    def get(self, request, format=None):
        account =User.objects.filter(is_admin=True).all()
        serializer = UserSerializer(account, many=True)
        return Response(serializer.data)

#@admin_only
class dep(APIView):
    serializer_class=departmentSerializer
    #@customer_required(login_url='api/auth/login', redirect_field_name='', message='You are not authorised to view this page.')
    def get(self, request, format=None):
        dept = department.objects.all()
        serializer = departmentSerializer(dept, many=True)
        return Response(serializer.data)
  
    #@customer_required(login_url='api/auth/login', redirect_field_name='', message='You are not authorised to view this page.')
    def post(self, request, format=None):
        serializer = departmentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,
                            status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class UserLoginView(APIView):
    serializer_class=UserLoginSerializer
    def post(self, request):
        ser_data =UserLoginSerializer(data=request.POST)
        if ser_data.is_valid():
            data = ser_data.validated_data
            user = User.objects.get(identification_number=data['identification_number'])
        
            if user:
                if user.check_password(data['password']):
                    login(request, user)
                    user.save()
                    if request.user.is_staff is False:
                        userRole="is_User"
                    else:
                        userRole="isAdmin"
                    return Response({'message':"successfully logged in",
                        'user_role':userRole})
                return Response({'detail': 'inter password'})
            return Response({'detail': 'user does not exists'})
        return Response(ser_data.errors, status=status.HTTP_400_BAD_REQUEST)

class UserLogoutView(APIView):

    def post(self, request):
        ser_data =UserLogoutSerializer(data=request.POST)
        if ser_data.is_valid():
            data = ser_data.validated_data
            user = User.objects.get(identification_number=data['identification_number'])
            if user:
                logout(request)
                return Response(ser_data.data, status=status.HTTP_200_OK)
            return Response({'detail': 'user does not exists'})
        return Response(ser_data.errors, status=status.HTTP_400_BAD_REQUEST)
    

class admin_dashboard(APIView):
    authentication_classes=[SessionAuthentication]
    permission_classes=[AllowAny] 
    def get(self,request):
        user=User.objects.all()
        # app_model=appo.appointment 
        app=appo.appointment.objects.all()

        total_user=user.filter(is_customer=True).count()
        total_appointment=app.count()
        # delivered= order.filter(status='delivered').count()
        pending= app.filter(pending=True).count()
        approved= app.filter(status=True).count()
        declined= app.filter(status=False).count()
        context={'users':user,'apps':app,'total_user':total_user,'total_appointment':total_appointment,pending:'pending',approved:'approved',declined:'declined'}
        return render(request, 'admin_dashboard.html',context)
# class UserViewSet(ModelViewSet):
#     serializer_class = UserSerializer
#     queryset = User.objects.all()

#     # you can define permissions at the view level
#     view_permissions = {
#         'create': {'anon': True},  # only anonymous visitors allowed
#         'list': {'admin': True}, 
#         'retrieve,me': {'user': is_self},
#         'update,update_partial': {'user': is_self, 'admin': True},
#     }

#     @action(detail=False, methods=['get'])
#     def me(self, request):
#         self.kwargs['pk'] = request.user.pk
#         return self.retrieve(request)
def IsAdmin(self,request):
    # search_fields = ['is_staff']
            
    if self.request.user.is_staff is True:
        return Response({
            "is_staff": "True", })
def IsUser(self,request):
    # search_fields = ['is_staff']
    if self.context['request'].user.is_staff is False:
        return Response({
            "is_staff": "False", })

# def IsUser(request):
#     # search_fields = ['is_staff']
#     if request.session['is_staff'] is False:
#         return Response({
#             "is_staff": "False", })


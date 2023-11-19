# from datetime import timezone
from django.utils import timezone
from datetime import *
from pyexpat.errors import messages
from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import redirect, render
from django.http import Http404, HttpResponse
from rest_framework.views import APIView
from rest_framework.authtoken.models import Token
from Auth import models as auth_model
from .models import appointment
from .serializers import appSerializer,appointmentStatus
from rest_framework import filters
from Auth.views import UserLoginView
from django.contrib.auth.decorators import login_required
from services import models as serv_model



class schedule_app_servid(APIView):
    serializer_class=appSerializer
    def post(self, request,pk, format=None):
        # pk= self.kwargs.get('pk')
        serv=serv_model.services.objects.get(ID=pk) 
        app_form = appSerializer(data=request.data)
        # data = ser_data.validated_data
        # task=Task.objects.get(id=pk)
        # serializer=TaskSerializer(instance=task,data=request.data)
        

        if app_form.is_valid():  
            data = app_form.validated_data
            app_date=data['app_date']
            service_=serv.name
            # dep_ID=data['dep_ID'] 
            if datetime.now().date() < app_date: 
                count_app=appointment.objects.filter(app_date=data['app_date'], service_ID=service_).count()
                # count_app=appointment.objects.filter(app_date=data['app_date'], dep_ID=data['dep_ID']).count()
                if count_app<=5:            
                    appointment.service_ID=serv.name     
                    app_form.save(request,appointment.service_ID)
                    # appointment.save() 
                    # messages.add_message(request, messages.INFO, 'Your appointment is received and pending.')
                    return Response({'Your appointment is received and pending.'})
                
                else:
                    return Response({'appointment date is full!!!'})
            else:
                return Response({'Invalid date.'})
            
        return Response(app_form.errors, status=status.HTTP_400_BAD_REQUEST)


class schedule_app(APIView):
    serializer_class=appSerializer
    def post(self, request, format=None): 
        app_form = appSerializer(data=request.data)
        if app_form.is_valid():  
            data = app_form.validated_data
            app_date=data['app_date']
            # dep_ID=data['dep_ID'] 
            if datetime.now().date() < app_date: 
            #     july_aug=(1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19.20,21,22,23,24,25,26,27,28,29,30,31)
            #     sep=(1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19.20,21,22,23,24,25,26,27,28,29,30)
            #     for i in range(len(july_aug)):
            #         # july_aug[i]
            #         datee_in = datetime.datetime.strptime(app_date, "%Y-%m-%d")
            #         datee_db = datetime.datetime.strptime(data['app_date'], "%Y-%m-%d")
            #         datee_db.month
            #         datee_db.day
            #         monthh=datee_in.month
            #         dayy=datee_in.day
            #         count_app=appointment.objects.filter(monthh=datee_db.month, dayy=july_aug[i], dep_ID=data['dep_ID']).count()
                count_app=appointment.objects.filter(app_date=data['app_date'], dep_ID=data['dep_ID']).count()
                if count_app<=5:                   
                    app_form.save(request)
                    # messages.add_message(request, messages.INFO, 'Your appointment is received and pending.')
                    return Response({'Your appointment is received and pending.'})
                
                else:
                    return Response({'appointment date is full!!!'})
            else:
                return Response({'Invalid date.'})
            
        return Response(app_form.errors, status=status.HTTP_400_BAD_REQUEST)
    
class approve_app(APIView):
    def post(request, pk):
            appoint = appointment.objects.get(id=pk)
            appoint.status = "approved"  # approve appointment
            # appoint.pending=False
            appoint.save()

            messages.success(request, "Appointment approved successfully.")
            # return redirect(reverse('view_all_app_adm.html'))

class decline_app(APIView):
    def decline_app(request, pk):
            appoint = appointment.objects.get(id=pk)
            appoint.status = "declined"  # decline appointment
            # appoint.pending=False
            appoint.save()

            messages.success(request, "Appointment declined successfully.")
 
class all_app(APIView):
    def  all_app(request):         
        app=appointment.objects.all()
        return render(request,{'appointments':app})

class Appointment_filter(generics.ListCreateAPIView):
    search_fields = ['ApprovalStatus']
    filter_backends = (filters.SearchFilter,)
    queryset = appointment.objects.all().filter(ApprovalStatus="pending")
    serializer_class = appointmentStatus

class Appointment_filter_approved(generics.ListCreateAPIView):
    search_fields = ['ApprovalStatus']
    filter_backends = (filters.SearchFilter,)
    queryset = appointment.objects.all().filter(ApprovalStatus="approved")
    serializer_class = appointmentStatus
    
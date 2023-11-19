from rest_framework import serializers
from .models import appointment
from services import models as serv_model

class appSerializer(serializers.ModelSerializer):
    class Meta:
        model = appointment
        # fields=['service_ID','dep_ID','app_date']
        fields=['app_date']
        
  
    def save(self,request,*args, **kwargs):
        # *args, **kwargs
        # pk= self.kwargs.get('pk')
        # serv=serv_model.services.objects.get(ID=pk)
        user_id = request.user.identification_number
        request.session['user_id'] = user_id
        appo=appointment(
            service_ID=appointment.service_ID,
            # service_ID=self.validated_data['service_ID'],
            # dep_ID=self.validated_data['dep_ID'],
            app_date=self.validated_data['app_date'],
            customer_ID= request.session['user_id']
        )
        appo.save()
        return appo
    
class appointmentStatus(serializers.ModelSerializer):
    class Meta:
        model = appointment
        fields = '__all__'
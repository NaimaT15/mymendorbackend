from rest_framework import serializers
from .models import Form,FormField,Datatype
class FormSerializer(serializers.ModelSerializer):
    class Meta:
        model = Form
        fields = ('department_id','service_id','field_id',)
        
class FormFieldSerializer(serializers.ModelSerializer):
    class Meta:
        model = FormField
        fields = ('field_name','datatype_id',)
        
class DataTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Datatype
        fields = ('name',)
        
                             
from rest_framework import serializers
from .models import services, general_requirment

class ServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = services
        fields=('__all__')

class RequirmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = general_requirment
        fields=('__all__')
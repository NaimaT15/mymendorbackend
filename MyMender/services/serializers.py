from rest_framework import serializers
from .models import services, general_requirment
from rest_framework.serializers import ModelSerializer
from rest_framework import exceptions
class ServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = services
        fields=('__all__')

class RequirmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = general_requirment
        fields=('__all__')
# class Admmin_serviceSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = admin_services
#         fields=('__all__')

class UpdateServiceSerializer(ModelSerializer):

    def validate(self, data):
        # author = self.context['author']
        if "#" in data['title']:
            raise exceptions.ValidationError(detail="can not include '#' in title")  # NOQA
        return data

    def update(self, instance, validated_data):
        instance.title = validated_data.get('title', instance.title)
        instance.save()
        return instance

    class Meta:
        model = services
        fields = '__all__'
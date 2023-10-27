from rest_framework import serializers
from .models import announcement

class announceSerializer(serializers.ModelSerializer):
    class Meta:
        model = announcement
        fields=('__all__')


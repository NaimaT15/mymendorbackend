from rest_framework import serializers
from .models import Bid


class BidSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bid
        fields = ('title','price')
class CreateBidSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bid
        fields = ('title','price','description','initial_price','end_time','start_time','winner','final_price','numberOfExperience',)

from rest_framework import serializers
from .models import Bid
from .models import Commpetition

class BidInitSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bid
        fields = ('title','description','initial_price')
class BidCommpSerializer(serializers.ModelSerializer):
    class Meta:
        model = Commpetition
        fields = ('final_price',)
class BidWinnerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Commpetition
        fields = ('bid_id','customer_id')


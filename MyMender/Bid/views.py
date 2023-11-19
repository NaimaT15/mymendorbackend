from django.shortcuts import render
from .serializer import BidInitSerializer,BidCommpSerializer,BidWinnerSerializer
# from .serializer import CreateBidSerializer,CreatedSerializer
from rest_framework.response import Response
from rest_framework import status, generics
from .models import Bid
from rest_framework.views import APIView
from .models import Commpetition
import datetime
from django.http import HttpResponse
class BidInitialization(generics.GenericAPIView):
    serializer_class = BidInitSerializer
    queryset = Bid.objects.all()
    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"status": "success", "Bid": serializer.data}, status=status.HTTP_201_CREATED)
        else:
            return Response({"status": "fail", "message": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
class BidCommpitionInfo(generics.GenericAPIView):
    serializer_class=BidCommpSerializer
    queryset = Commpetition.objects.all()
    def post(self,request):
        serializer1 = self.serializer_class(data=request.data)    
        if serializer1.is_valid():
            # if request.
            
            serializer1.save()
            return Response({"status": "success", "Bid": serializer1.data}, status=status.HTTP_201_CREATED)
        else:
            return Response({"status": "fail", "message": serializer1.errors}, status=status.HTTP_400_BAD_REQUEST)
        

def testing(request):
  mydata = Bid.objects.values_list('price')
  context = {
    'price': mydata, 
  }

  return HttpResponse(context, request)

class BidWinner(generics.GenericAPIView):
    serializer_class = BidWinnerSerializer
    queryset = Commpetition.objects.all()
    def get(self, request):
        winnerByPrice = Commpetition.objects.order_by('-final_price')[0]
        # winnerByExperiance=Commpetition.objects.order_by('-numberOfExperience')
        serializer = self.serializer_class()
        
        
        return Response({
            "status": "success",
            "winnerr":winnerByPrice.final_price,
            "winner_id":winnerByPrice.winner_id,
            "bid_id":winnerByPrice.bid_id,
        })

class Bid_list(APIView):
    serializer_class=BidInitSerializer
    def get(self, request, format=None):
        bid = Bid.objects.all()
        serializer = BidInitSerializer( bid, many=True)
        return Response(serializer.data)


class FindByBidID(generics.ListCreateAPIView):
   serializer_class = BidInitSerializer
   filter_class = Bid_list
   def get_queryset(self):
      queryset = Bid.objects.filter(pk=self.kwargs['post_id'])
      return queryset
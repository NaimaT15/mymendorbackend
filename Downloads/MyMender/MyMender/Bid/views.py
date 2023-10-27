from django.shortcuts import render
from .serializer import BidSerializer
from .serializer import CreateBidSerializer
from rest_framework.response import Response
from rest_framework import status, generics
from .models import Bid
from Bid.models import BidInfo
class CreateBid(generics.GenericAPIView):
    serializer_class = BidSerializer
    queryset = Bid.objects.all()
    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"status": "success", "Bid": serializer.data}, status=status.HTTP_201_CREATED)
        else:
            return Response({"status": "fail", "message": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
class BidInitialization(generics.GenericAPIView):
    serializer_class=CreateBidSerializer
    queryset = BidInfo.objects.all()
    def Post1(self,request):
        serializer1 = self.serializer_class(data=request.data)
        
        if serializer1.is_valid():
            serializer1.save()
            return Response({"status": "success", "Bid": serializer1.data}, status=status.HTTP_201_CREATED)
        else:
            return Response({"status": "fail", "message": serializer1.errors}, status=status.HTTP_400_BAD_REQUEST)


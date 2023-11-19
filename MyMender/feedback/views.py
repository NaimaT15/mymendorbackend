from django.shortcuts import render
from .serializer import FeedbackSerializer
from rest_framework.response import Response
from rest_framework import status, generics
from .models import Feedback
from django.conf import settings
from twilio.rest import Client
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated, AllowAny, IsAdminUser

def send_text():
  client = Client(settings.TWILIO_ACCOUNT_SID, settings.TWILIO_AUTH_TOKEN )
  message = client.messages.create(
      to= "+251910493259", 
      from_="+14066294771", # insert trial number 
      body="Hey I hope you received this message") # insert message

class CreateFeedback(generics.GenericAPIView):
    
    serializer_class = FeedbackSerializer
    queryset = Feedback.objects.all()
    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            send_text()
            serializer.save()

            return Response({"status": "success", "Feedback": serializer.data}, status=status.HTTP_201_CREATED)
        else:
            return Response({"status": "fail", "message": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)


class FeedBack_list(APIView):
    serializer_class=FeedbackSerializer
    permission_classes=[IsAuthenticated] 

    def get(self, request, format=None):
        feedback = Feedback.objects.all()
        serializer = FeedbackSerializer( feedback, many=True)
        return Response(serializer.data)





































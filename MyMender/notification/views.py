from django.shortcuts import render

from .serializer import NotificationSerializer
from rest_framework.response import Response
from rest_framework import status, generics
from .models import Notification
from Auth.models import customer,User

class AddNotification(generics.GenericAPIView):
    serializer_class = NotificationSerializer
    queryset = Notification.objects.all()
    customer1 = customer.objects.all()
    user1=User.objects.all()
    for r in customer1:
        print(r.customer_id.user_ID.first_name)
    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"status": "success", "Feedback": serializer.data}, status=status.HTTP_201_CREATED)
        else:
            return Response({"status": "fail", "message": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)



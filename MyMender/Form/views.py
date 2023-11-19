from django.shortcuts import render
from rest_framework import status, generics
from .serializer import FormSerializer,FormFieldSerializer,DataTypeSerializer
from rest_framework.response import Response

from .models import Form,FormField,Datatype
class AddForm(generics.GenericAPIView):
    serializer_class = FormSerializer
    queryset = Form.objects.all()
    
    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"status": "success", "Form": serializer.data}, status=status.HTTP_201_CREATED)
        else:
            return Response({"status": "fail", "message": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
class AddFormField(generics.GenericAPIView):
    serializer_class = FormFieldSerializer
    queryset = FormField.objects.all()
    
    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"status": "success", "FormField": serializer.data}, status=status.HTTP_201_CREATED)
        else:
            return Response({"status": "fail", "message": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
class AddDatatype(generics.GenericAPIView):
    serializer_class = DataTypeSerializer
    queryset = Datatype.objects.all()
    
    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"status": "success", "DataType": serializer.data}, status=status.HTTP_201_CREATED)
        else:
            return Response({"status": "fail", "message": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)





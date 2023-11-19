# from django.test import TestCase
# class AddService(generics.GenericAPIView):
#     serializer_class = ServiceSerializer
#     queryset = Service.objects.all()
#     def post(self, request):
#         serializer = self.serializer_class(data=request.data)
#         serializer = self.serializer_class(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response({"status": "success", "Feedback": serializer.data}, status=status.HTTP_201_CREATED)
#         else:
#             return Response({"status": "fail", "message": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

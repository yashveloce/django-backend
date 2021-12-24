from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Student
from .serializers import StudentSerializer

# Create your views here.
class StudentCRUD(APIView):
    def post(self, request):
        serializer = StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)
        else:
            return Response({"status": "error", "data": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
    # def post(self,request):
    #     name = request.data['name']
    #     email = request.data['email']
    #     roll_no = request.data['roll_no']
    #     if request.data:
    #         student = Student(name=name,email=email,roll_no=roll_no)
    #         student.save()
    #         return Response({"status": "success", "data": "Data Inserted"}, status=status.HTTP_200_OK)
    #     else:
    #         return Response({"status": "error", "data": "Cannot create object"}, status=status.HTTP_400_BAD_REQUEST)

    def get(self,request):
        studentdata = Student.objects.all()
        if studentdata:
            serializer = StudentSerializer(studentdata,many=True)
            return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)
        else:
            return Response({"status": "error", "data":studentdata.error}, status=status.HTTP_400_BAD_REQUEST)

    def patch(self,request):
        studentitem = Student.objects.get(id=request.data['id'])
        serializer = StudentSerializer(studentitem, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)
        else:
            return Response({"status": "error", "data": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request):
        item = Student.objects.get(id=request.data['id'])
        item.delete()
        return Response({"status": "success", "data": "Item Deleted"})
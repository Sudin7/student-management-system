from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from students.models import degree
from .serializers import DegreeSerializer


class DegreeView(APIView):

    def get(self, request):
        degrees = degree.objects.all()
        serializer = DegreeSerializer(degrees, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = DegreeSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)

        return Response(serializer.errors, status=400)

    def put(self, request, pk):
        degree_obj = degree.objects.get(id=pk)

        serializer = DegreeSerializer(degree_obj, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

        return Response(serializer.errors, status=400)




from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from students.models import Student
from .serializers import StudentSerializer


class StudentView(APIView):

    # GET: View all students
    def get(self, request):
        students = Student.objects.all()

        serializer = StudentSerializer(students, many=True)

        return Response(serializer.data)

    # POST: Create a new student
    def post(self, request):
        serializer = StudentSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)

        return Response(serializer.errors, status=400)

    # PUT: Update an existing student
    def put(self, request, pk):
        student = Student.objects.get(pk=pk)

        serializer = StudentSerializer(student, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

        return Response(serializer.errors, status=400)

    # DELETE: Delete an existing student
    def delete(self, request, pk):
        student = Student.objects.get(pk=pk)

        student.delete()

        return Response({"message": "Student deleted successfully"})

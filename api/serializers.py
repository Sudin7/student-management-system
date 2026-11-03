from students.models import Student, degree
from rest_framework import serializers

class DegreeSerializer(serializers.ModelSerializer):
    class Meta:
        model=degree
        fields='__all__'

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model=Student
        fields='__all__'
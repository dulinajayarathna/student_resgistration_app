from rest_framework import viewsets
from rest_framework.response import Response
from .models import Student
from .serializers import StudentSerializer


class StudentViewSet(viewsets.ModelViewSet):  # Define the queryset to retrieve all Student objects from the database
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

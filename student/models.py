from django.db import models


class Student(models.Model):
    """
    A model representing a student with the following attributes:
    - first_name: The student's first name (max length: 20 characters)
    - last_name: The student's last name (max length: 20 characters)
    - dob: The student's date of birth
    - email: The student's unique email address
    """
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    dob = models.DateField()
    email = models.EmailField(unique=True)

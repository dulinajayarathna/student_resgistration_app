from rest_framework import serializers

from student.models import Student


class StudentSerializer(serializers.ModelSerializer):
    """
      Serializer class for the Student model.

      This serializer is used to convert Student model instances into
      representations such as JSON and vice versa. It includes the following fields:
      - first_name: The student's first name (max length: 20 characters)
      - last_name: The student's last name (max length: 20 characters)
      - dob: The student's date of birth
      - email: The student's unique email address

      The Meta class specifies the model to be serialized and any additional options.
      """

    class Meta:
        model = Student
        fields = "_all_"

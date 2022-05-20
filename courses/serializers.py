from rest_framework import serializers

from accounts.serializers import AccountsSerializer

class CreateCoursesSerializer(serializers.Serializer):
    uuid = serializers.CharField(read_only=True)
    name = serializers.CharField()
    link_repo = serializers.CharField()
    demo_time = serializers.TimeField()

class CoursesSerializer(serializers.Serializer):
    uuid = serializers.CharField(read_only=True)
    name = serializers.CharField()
    link_repo = serializers.CharField()
    demo_time = serializers.TimeField()
    created_at = serializers.DateField(read_only=True)
    instructor = AccountsSerializer()
    students = AccountsSerializer(many=True)

class InstructorSerializer(serializers.Serializer):
    instructor_id = serializers.CharField()

class StudentSerializer(serializers.Serializer):
    students_id = serializers.ListField(child=serializers.UUIDField())

class UpdateCoursesSerializer(serializers.Serializer):
    uuid = serializers.CharField(read_only=True)
    name = serializers.CharField(required=False)
    link_repo = serializers.CharField(required=False)
    demo_time = serializers.TimeField(required=False)

class CourseUUIDSerializer(serializers.Serializer):
    course_id = serializers.UUIDField()
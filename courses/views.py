from black import nullcontext
from rest_framework.decorators import (
    api_view,
    authentication_classes,
    permission_classes,
)
from rest_framework import status
from rest_framework.authentication import TokenAuthentication
from rest_framework.decorators import api_view
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated

from courses.permissions import isAdmin
from courses.models import Courses
from accounts.models import MyUser
from courses.serializers import CourseUUIDSerializer, CoursesSerializer, CoursesSerializer, CreateCoursesSerializer, InstructorSerializer, StudentSerializer, UpdateCoursesSerializer

class CoursesView(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [isAdmin]

    def get(self, request:Request):

        courses = Courses.objects.all()
        serializer = CoursesSerializer(courses, many=True)

        return Response(serializer.data, status.HTTP_200_OK)

    def post(self, request: Request):
        serializer = CreateCoursesSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        found_course = Courses.objects.filter(
            name=serializer.validated_data["name"]
        ).exists()

        if found_course:
            return Response(
                {"message": "Course already exists"}, status.HTTP_422_UNPROCESSABLE_ENTITY
            )

        course = Courses.objects.create(**serializer.validated_data)
        course.save()

        serializer = CoursesSerializer(course)

        return Response(serializer.data, status.HTTP_201_CREATED)

class CoursesViewId(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [isAdmin]

    def get(self, request: Request, course_id:str):
        course = Courses.objects.filter(uuid=course_id).first()

        if not course:
            return Response(
                {"message": "Course does not exist"}, status.HTTP_404_NOT_FOUND
            )

        serializer = CoursesSerializer(course)

        return Response(serializer.data, status.HTTP_200_OK)


    def patch(self, request: Request, course_id:str):
        serializer = UpdateCoursesSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        try:
            course = Courses.objects.get(uuid=course_id)
        except Courses.DoesNotExist:
            return Response(
                {"message": "Course does not exist"}, status.HTTP_404_NOT_FOUND
            )

        course = Courses.objects.filter(uuid = course_id)

        if 'name' in serializer.data:
            found_course = Courses.objects.filter(
                name=serializer.validated_data["name"]
            ).exists()

            if found_course:
                return Response(
                    {"message": 'This course name already exists'}, status.HTTP_422_UNPROCESSABLE_ENTITY
                )

            course.update(name = serializer.data['name'])
        
        if 'demo_time' in serializer.data:
            course.update(demo_time = serializer.data['demo_time'])

        if 'link_repo' in serializer.data:
            course.update(link_repo = serializer.data['link_repo'])

        try:
            course = Courses.objects.get(uuid=course_id)
        except Courses.DoesNotExist:
            return Response(
                {"message": "Course does not exist"}, status.HTTP_404_NOT_FOUND
            )
        course = CoursesSerializer(course).data

        return Response(course, status.HTTP_200_OK)
    
    
    def delete(self, request: Request, course_id:str):
        serializer = CourseUUIDSerializer(data={"course_id": course_id})
        if not serializer.is_valid():
            return Response(
                {"message": "Not found."}, status.HTTP_404_NOT_FOUND
            )
        try:
            course = Courses.objects.get(uuid=course_id)
        except Courses.DoesNotExist:
            return Response(
                {"message": "Course does not exist"}, status.HTTP_404_NOT_FOUND
            )
        course.delete()

        return Response('',status.HTTP_204_NO_CONTENT)


@api_view(["PUT"])
@authentication_classes([TokenAuthentication])
@permission_classes([isAdmin])
def create_instructor(request: Request, course_id):
    instructor_serializer = InstructorSerializer(data=request.data)
    instructor_serializer.is_valid(raise_exception=True)

    try:
        instructor = MyUser.objects.get(uuid=instructor_serializer.validated_data['instructor_id'])
    except MyUser.DoesNotExist:
        return Response(
            {"message": 'Invalid instructor_id'}, status.HTTP_404_NOT_FOUND
        )

    if not instructor.is_admin:
        return Response({"message": "Instructor id does not belong to an admin"}, status.HTTP_422_UNPROCESSABLE_ENTITY)


    course_serializer = CourseUUIDSerializer(data={"course_id": course_id})
    if not course_serializer.is_valid():
        return Response(
            {"message": "Course does not exist"}, status.HTTP_404_NOT_FOUND
        )

    course = Courses.objects.filter(uuid = course_serializer.validated_data["course_id"]).first()
    
    if not course:
        return Response({"message": "Course does not exist"}, status.HTTP_404_NOT_FOUND)

    instructor_already_registered = Courses.objects.filter(instructor= instructor.uuid).first()

    if instructor_already_registered:
        instructor_already_registered.instructor = None
        instructor_already_registered.save()

    course.instructor = instructor
    course.save()

    try:
        course = Courses.objects.get(uuid=course_serializer.validated_data['course_id'])
    except Courses.DoesNotExist:
        return Response(
            {"message": "Course does not exist"}, status.HTTP_404_NOT_FOUND
        )
    course = CoursesSerializer(course)

    return Response(course.data, status.HTTP_200_OK)


@api_view(["PUT"])
@authentication_classes([TokenAuthentication])
@permission_classes([isAdmin])
def create_student(request: Request, course_id: str):
    students_serializer = StudentSerializer(data=request.data)
    students_serializer.is_valid(raise_exception=True)

    course_serializer = CourseUUIDSerializer(data={"course_id": course_id})
    if not course_serializer.is_valid():
        return Response(
            {"message": "Course does not exist"}, status.HTTP_404_NOT_FOUND
        )

    course = Courses.objects.filter(uuid = course_serializer.validated_data["course_id"]).first()

    if not course:
        return Response({"message": "Course does not exist"}, status.HTTP_404_NOT_FOUND)


    student_list = []
    for student_id in students_serializer.validated_data['students_id']:
        try:
            student = MyUser.objects.get(uuid=student_id)
        
        except MyUser.DoesNotExist:
            return Response(
                {"message": 'Invalid students_id list'}, status.HTTP_404_NOT_FOUND
            )

        if student.is_admin:
            return Response({"message":"Some student id belongs to an Instructor"}, status.HTTP_422_UNPROCESSABLE_ENTITY)

        student_list.append(student) 

    
    
    course.students.set(student_list)

    course = Courses.objects.get(uuid=course_serializer.data['course_id'])
    course = CoursesSerializer(course)


    return Response(course.data, status.HTTP_200_OK)
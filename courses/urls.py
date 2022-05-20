from django.urls import path

from courses.views import CoursesView, CoursesViewId, create_instructor, create_student

urlpatterns = [
    path("courses/", CoursesView.as_view()),
    path("courses/<course_id>/", CoursesViewId.as_view()),

    path("courses/<course_id>/registrations/instructor/", create_instructor),
    path("courses/<course_id>/registrations/students/", create_student)
]
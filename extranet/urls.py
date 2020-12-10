from django.urls import path

from . import views

urlpatterns = [
    path('', views.user_login, name='login'),
    # Student
    path('student', views.student_data, name='homeStudent'),
    path('student/grades', views.students_grades, name='studentGrades'),
    # Teacher
    path('teacher', views.teacher_data, name='homeTeacher'),
    path('teacher/courses', views.teacher_courses, name='teacherCourses')
]

from django.urls import path

from . import views

urlpatterns = [
    path('', views.user_login, name='home'),
    path('logout', views.user_logout, name='logout'),
    # Student
    path('student', views.student_data, name='studentHome'),
    path('student/grades', views.students_grades, name='studentGrades'),
    path('student/<str:index>', views.view_student_data, name='viewStudentProfile'),
    # Teacher
    path('teacher', views.teacher_data, name='teacherHome'),
    path('teacher/courses', views.teacher_courses, name='teacherCourses'),
    path('teacher/courses/<int:pk>', views.teacher_course, name='teacherCourse'),
]

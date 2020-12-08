from django.urls import path

from . import views

urlpatterns = [ 
    path('index', views.index, name='index'),
    path('login', views.user_login, name='login'),
    path('homeStudent', views.student_data, name='homeStudent'),
    path('homeTeacher', views.teacher_data, name='homeTeacher'),
    path('studentGrades',  views.students_grades, name='studentGrades'),
    path('teacherCourses',  views.teacher_courses, name='teacherCourses')
]

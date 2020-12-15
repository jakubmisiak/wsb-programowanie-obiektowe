from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout, REDIRECT_FIELD_NAME
from extranet.models.course import Course
from extranet.models.grade import Grade
from extranet.models.student import Student
from extranet.models.teacher import Teacher

LOGIN_PATH_NAME = 'home'


# Autoryzacja
def user_login(request):
    def redirect_user(authenticated_user):
        if Teacher.objects.filter(user=authenticated_user).exists():
            return redirect('teacherHome')
        else:
            return redirect('studentHome')

    if request.user.is_authenticated:
        return redirect_user(request.user)

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect_user(user)

        else:
            return redirect('home')

    else:
        return render(request, 'login.html')


def user_logout(request):
    logout(request)

    return redirect(LOGIN_PATH_NAME)


def allow_user_type(user_type, request):
    if not user_type.objects.filter(user=request.user).exists():
        return render(request, 'no_access.html')


# Student
@login_required(None, REDIRECT_FIELD_NAME, LOGIN_PATH_NAME)
def student_data(request):
    allow_user_type(Student, request)

    student = Student.objects.get(user=request.user)
    context = {
        "student": student
    }

    return render(request, 'student/home.html', context)


@login_required(None, REDIRECT_FIELD_NAME, LOGIN_PATH_NAME)
def students_grades(request):
    allow_user_type(Student, request)

    student = Student.objects.get(user=request.user)
    context = {
        "grades": Grade.objects.filter(student=student).all()
    }

    return render(request, 'student/grades.html', context)


# Teacher
@login_required(None, REDIRECT_FIELD_NAME, LOGIN_PATH_NAME)
def teacher_data(request):
    allow_user_type(Teacher, request)

    teacher = Teacher.objects.get(user=request.user)
    context = {
        "teacher": teacher
    }

    return render(request, 'teacher/home.html', context)


@login_required(None, REDIRECT_FIELD_NAME, LOGIN_PATH_NAME)
def teacher_courses(request):
    allow_user_type(Teacher, request)

    teacher = Teacher.objects.get(user=request.user)
    current_course_data = Course.objects.filter(teacher=teacher).all()
    context = {
        "object_list": current_course_data
    }

    return render(request, 'teacher/courses.html', context)


@login_required(None, REDIRECT_FIELD_NAME, LOGIN_PATH_NAME)
def view_student_data(request, index):
    allow_user_type(Teacher, request)

    try:
        student = Student.objects.get(index=index)
        context = {
            "student": student
        }

        return render(request, 'student/profile.html', context)

    except Student.DoesNotExist:
        return render(request, 'not_found.html')

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


def is_student(user):
    return Student.objects.filter(user=user).exists()


def is_teacher(user):
    return Teacher.objects.filter(user=user).exists()


def render_no_access_page(request):
    return render(request, 'no_access.html')


# Student
@login_required(None, REDIRECT_FIELD_NAME, LOGIN_PATH_NAME)
def student_data(request):
    if not is_student(request.user):
        return render_no_access_page(request)

    student = Student.objects.get(user=request.user)
    context = {
        "student": student
    }

    return render(request, 'student/home.html', context)


@login_required(None, REDIRECT_FIELD_NAME, LOGIN_PATH_NAME)
def students_grades(request):
    if not is_student(request.user):
        return render_no_access_page(request)

    student = Student.objects.get(user=request.user)
    courses = Course.objects.filter(student_group=student.student_group).all()
    grades = []

    if courses:
        grades = Grade.objects.filter(student=student).all()

    context = {
        "courses": courses,
        "grades": grades,
    }

    return render(request, 'student/grades.html', context)


@login_required(None, REDIRECT_FIELD_NAME, LOGIN_PATH_NAME)
def view_teacher_data(request, pk):
    if not request.user.is_authenticated:
        return redirect(LOGIN_PATH_NAME)

    try:
        teacher = Teacher.objects.get(pk=pk)
        context = {
            "teacher": teacher
        }

        return render(request, 'teacher/profile.html', context)

    except Teacher.DoesNotExist:
        return render(request, 'not_found.html')


# Teacher
@login_required(None, REDIRECT_FIELD_NAME, LOGIN_PATH_NAME)
def teacher_data(request):
    if not is_teacher(request.user):
        return render_no_access_page(request)

    teacher = Teacher.objects.get(user=request.user)
    context = {
        "teacher": teacher
    }

    return render(request, 'teacher/home.html', context)


@login_required(None, REDIRECT_FIELD_NAME, LOGIN_PATH_NAME)
def teacher_courses(request):
    if not is_teacher(request.user):
        return render_no_access_page(request)

    teacher = Teacher.objects.get(user=request.user)
    courses = Course.objects.filter(teacher=teacher).all().order_by('student_group__name', 'name')
    context = {
        "courses": courses
    }

    return render(request, 'teacher/courses.html', context)


@login_required(None, REDIRECT_FIELD_NAME, LOGIN_PATH_NAME)
def teacher_course(request, pk):
    try:
        teacher = Teacher.objects.get(user=request.user)
        course = Course.objects.get(pk=pk, teacher=teacher)
        grades = Grade.VALUES
        students = Student.objects.filter(student_group=course.student_group).all().order_by('index')
        student_grades = Grade.objects.filter(course=course).all()
        context = {
            "course": course,
            "grades": grades,
            "student_grades": student_grades,
            "students": students
        }

        return render(request, 'teacher/course.html', context)
    except Course.DoesNotExist:
        return render(request, 'not_found.html')


@login_required(None, REDIRECT_FIELD_NAME, LOGIN_PATH_NAME)
def update_course_grades(request, pk):
    if not request.method == 'POST':
        return redirect('teacherCourse', pk)

    try:
        teacher = Teacher.objects.get(user=request.user)
        course = Course.objects.get(pk=pk, teacher=teacher)
        form_data = request.POST.copy()

        del form_data["csrfmiddlewaretoken"]

        for field_name in form_data:
            student_id = field_name[-1:]
            student = Student.objects.get(pk=student_id)
            new_grade_value = float(form_data[field_name])

            if new_grade_value > 0.0:
                try:
                    grade = Grade.objects.get(course=course, student=student)
                    print(grade.student.user.get_full_name(), grade.value, new_grade_value)
                    grade.value = new_grade_value
                    grade.save()
                except Grade.DoesNotExist:
                    new_grade = Grade()
                    new_grade.course = course
                    new_grade.student = student
                    new_grade.value = new_grade_value
                    print("new_grade", new_grade.value)
                    new_grade.save()

        return redirect("teacherCourse", pk)

    except (Teacher.DoesNotExist, Course.DoesNotExist, Student.DoesNotExist):
        return redirect("teacherCourse", pk)


@login_required(None, REDIRECT_FIELD_NAME, LOGIN_PATH_NAME)
def view_student_data(request, index):
    if not is_teacher(request.user):
        return render_no_access_page(request)

    try:
        student = Student.objects.get(index=index)
        context = {
            "student": student
        }

        return render(request, 'student/profile.html', context)

    except Student.DoesNotExist:
        return render(request, 'not_found.html')

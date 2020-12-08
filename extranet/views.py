from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate,login
from extranet.models.course import Course
from extranet.models.grade import Grade
from extranet.models.student import Student
from extranet.models.teacher import Teacher


def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            if Teacher.objects.filter(user=user).exists():
                return redirect('homeTeacher')
            else:
                return redirect('homeStudent')

        else:
            return redirect('login')

    else:
        return render(request, 'login.html')

def index(request):
    XD = '123'
    return render(request, 'index.html', {'XD':XD})

@login_required
def teacher_data(request):
    current_user = request.user
    if Teacher.objects.filter(user=current_user).exists():
        log_teacher = Teacher.objects.get()
        current_title = log_teacher.title
    return render(request, 'teacherHome.html', {'curent_title':current_title})

@login_required
def student_data(request):
    current_user = request.user
    if Student.objects.filter(user=current_user).exists():
        log_student = Student.objects.get()
        current_index = log_student.index
        current_group = log_student.student_group

    return render(request, 'userHome.html', {'current_index':current_index})

@login_required
def students_grades(request):
    current_user = request.user
    if Student.objects.filter(user=current_user).exists():
        log_student = Student.objects.get()
        if Grade.objects.filter(student= log_student).exists():
            current_grade_data = Grade.objects.all()
            context = {
                "object_list": current_grade_data
            }
            return render(request, 'studentGrades.html', context)


@login_required
def teacher_courses(request):
    current_user = request.user
    if Teacher.objects.filter(user=current_user).exists():
        log_teacher = Teacher.objects.get()
        if Course.objects.filter(teacher =log_teacher).exists():
            current_course_data = Course.objects.all()
            context = {
                "object_list": current_course_data
            }
            return render(request, 'teacherCourses.html', context)
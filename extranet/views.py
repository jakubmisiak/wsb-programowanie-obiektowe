from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate,login
from extranet.models import teacher
from extranet.models.student import Student
from extranet.models.teacher import Teacher


def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)

            print(user)
            if Teacher.objects.filter(user=user).exists():
                return redirect('homet')
            else:
                return redirect('homes')

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
        print(current_title)

    text = 'Jestem nauczycielem'
    return render(request, 'teacherData.html', {'curent_title':current_title})

@login_required
def student_data(request):
    current_user = request.user
    if Student.objects.filter(user=current_user).exists():
        log_student = Student.objects.get()
        current_index = log_student.index
        current_group = log_student.group
        print(current_index)
    text = 'Jestem studentem'
    return render(request,'userData.html', {'current_index':current_index})

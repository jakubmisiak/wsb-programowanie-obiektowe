from django.shortcuts import render, redirect
from django.contrib.auth import authenticate,login




def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('index')
        else:
            return redirect('login')

    else:
        return render(request, 'login.html')



def index(request):
    XD = '123'
    return render(request, 'index.html', {'XD':XD})

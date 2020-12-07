from django.urls import path

from . import views

urlpatterns = [

    path('index', views.index, name='index'),
    path('login', views.user_login, name='login' )

]
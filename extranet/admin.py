from django.contrib import admin
from .models.student import Student
from .models.group import Group

admin.site.register(Group)
admin.site.register(Student)
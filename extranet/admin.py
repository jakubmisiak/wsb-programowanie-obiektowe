from django.contrib import admin

from .models.course import Course
from .models.grade import Grade
from .models.group import Group
from .models.student import Student
from .models.teacher import Teacher

admin.site.register(Group)
admin.site.register(Student)
admin.site.register(Teacher)
admin.site.register(Course)
admin.site.register(Grade)

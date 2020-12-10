from django.contrib import admin

from .models.course import Course
from .models.grade import Grade
from .models.student_group import StudentGroup
from .models.student import Student
from .models.teacher import Teacher

admin.site.register(StudentGroup)
admin.site.register(Student)
admin.site.register(Teacher)
admin.site.register(Course)
admin.site.register(Grade)

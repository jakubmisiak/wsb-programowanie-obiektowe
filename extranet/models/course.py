from django.db import models
from extranet.models.studentGroup import StudentGroup
from extranet.models.teacher import Teacher


class Course(models.Model):
    name = models.CharField(max_length=255)
    student_group = models.ForeignKey(StudentGroup, on_delete=models.CASCADE, null=True)
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE, null=True)

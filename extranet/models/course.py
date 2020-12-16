from django.db import models
from extranet.models.student_group import StudentGroup
from extranet.models.teacher import Teacher


class Course(models.Model):
    name = models.CharField(max_length=255)
    student_group = models.ForeignKey(StudentGroup, on_delete=models.CASCADE, null=True)
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return f"{self.name} {self.teacher.user.get_full_name()}"

from django.db import models
from django.contrib.auth.models import User
from extranet.models.studentGroup import StudentGroup


class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    index = models.CharField(max_length=5, blank=False)
    student_group = models.ForeignKey(StudentGroup, on_delete=models.CASCADE, null=True)
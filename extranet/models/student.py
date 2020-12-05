from django.db import models
from django.contrib.auth.models import User, Group


class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    index = models.CharField(max_length=5, blank=False)
    group = models.ForeignKey(Group, on_delete=models.CASCADE, null=True)
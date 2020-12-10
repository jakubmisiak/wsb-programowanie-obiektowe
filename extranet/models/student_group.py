from django.db import models


class StudentGroup(models.Model):
    name = models.CharField(max_length=30)

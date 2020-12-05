from django.db import models
from django.contrib.auth.models import User


class Teacher(models.Model):
    INZYNIER = 'inz'
    DOKTOR = 'dr'
    MAGISTER = 'mgr'
    PROFESOR = 'prof'
    TEACHER_TITLE_CHOICE = [
        (DOKTOR, 'dr'),
        (INZYNIER, 'inz'),
        (MAGISTER, 'mgr'),
        (PROFESOR, 'prof')
    ]

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    title = models.CharField(choices=TEACHER_TITLE_CHOICE, max_length=8, null=True)

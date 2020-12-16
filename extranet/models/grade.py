from django.db import models

from extranet.models.course import Course
from extranet.models.student import Student


class Grade(models.Model):
    NDST = 2.0
    DST = 3.0
    DST_PLUS = 3.5
    DB = 4.0
    DB_PLUS = 4.5
    BDB = 5.0
    VALUES = [
        (NDST, '2.0'),
        (DST, '3.0'),
        (DST_PLUS, '3.5'),
        (DB, '4.0'),
        (DB_PLUS, '4.5'),
        (BDB, '5.0'),
    ]
    value = models.FloatField(choices=VALUES, null=True)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    student = models.ForeignKey(Student, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.course.name} - {self.student.index}"

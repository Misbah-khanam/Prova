from django.db import models
from user.models import User
from django.utils import timezone

class Exam(models.Model):
    subject_name =  models.CharField(max_length=100)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    uploaded_date = models.DateTimeField(auto_now=True)
    valid_till = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.subject_name 


class Question(models.Model):
    question = models.CharField(max_length=500)
    option_1 = models.CharField(max_length=100)
    option_2 = models.CharField(max_length=100)
    option_3 = models.CharField(max_length=100)
    option_4 = models.CharField(max_length=100)
    answer = models.CharField(max_length=100)
    exam = models.ForeignKey(Exam, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.question


class Attempted(models.Model):
    exam = models.ForeignKey(Exam, on_delete=models.SET_NULL, null=True)
    student = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    marks = models.CharField(max_length=100)
    attempt_date = models.DateTimeField()

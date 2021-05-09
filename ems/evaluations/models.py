from django.db import models
from users.models import Employee
from django.utils import timezone


class Criteria(models.Model):
    title = models.CharField(max_length=100)
    rating = models.IntegerField()
    comment = models.TextField()


class Evaluation(models.Model):
    employee = models.ForeignKey(
        Employee, on_delete=models.CASCADE, related_name="employee")
    evaluator = models.ForeignKey(
        Employee, on_delete=models.RESTRICT, related_name="evaluator")
    start_period = models.DateField(default=timezone.now)
    end_period = models.DateField(default=timezone.now)
    criteria = models.ManyToManyField(Criteria)

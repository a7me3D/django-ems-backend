from django.db import models
from users.models import Employee
from django.utils import timezone


class CriteriaType(models.Model):
    title = models.CharField(max_length=100)


class Criteria(models.Model):
    title = models.ForeignKey(CriteriaType, on_delete=models.CASCADE)
    rating = models.IntegerField(blank=True, null=True)
    comment = models.TextField(blank=True, null=True)


class Evaluation(models.Model):
    employee = models.ForeignKey(
        Employee, on_delete=models.CASCADE, related_name="employee")
    evaluator = models.ForeignKey(
        Employee, on_delete=models.RESTRICT, related_name="evaluator")
    start_period = models.DateField(default=timezone.now)
    end_period = models.DateField(default=timezone.now)
    criteria = models.ManyToManyField(Criteria)

from django.db import models
from django.utils import timezone


class CriteriaType(models.Model):
    title = models.CharField(max_length=100)

    def __str__(self):
        return self.title


class Criteria(models.Model):
    title = models.ForeignKey(CriteriaType, on_delete=models.CASCADE)
    rating = models.IntegerField(blank=False)
    comment = models.TextField(blank=False)


class Evaluation(models.Model):
    employee = models.ForeignKey(
        "users.Employee", on_delete=models.CASCADE, related_name="employee")
    evaluator = models.ForeignKey(
        "users.Employee", on_delete=models.RESTRICT, related_name="evaluator")
    start_period = models.DateField(default=timezone.now, blank=False)
    end_period = models.DateField(default=timezone.now, blank=False)
    criteria = models.ManyToManyField(Criteria)

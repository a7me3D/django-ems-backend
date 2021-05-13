from django.db import models
from django.utils import timezone
from users.models import Employee


def one_day_hence():
    return timezone.now() + timezone.timedelta(days=1)


class Conge(models.Model):
    CONGE_TYPE = [
        ("A", "annuel"),
        ("E", "exceptionnel"),
        ("M", "maladie"),
        ("R", "recuperation"),
    ]

    STATUS_TYPE = [
        ("P", "En attente"),
        ("A", "Accepté"),
        ("R", "Refusé"),
    ]

    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    demand_date = models.DateField(default=timezone.now, blank=False)
    start_date = models.DateField(default=timezone.now, blank=False)
    end_date = models.DateField(default=one_day_hence, blank=False)
    conge_type = models.CharField(
        max_length=1, choices=CONGE_TYPE, default=CONGE_TYPE[0][0])

    status = models.CharField(
        max_length=2, choices=STATUS_TYPE, default=STATUS_TYPE[0][0])

    @property
    def days(self):
        return (self.end_date - self.start_date).days


class CongeTitle(models.Model):
    conge = models.ForeignKey(Conge, on_delete=models.CASCADE)
    interim = models.ForeignKey(Employee, on_delete=models.CASCADE)
    solde = models.IntegerField(default=30)

    @property
    def rest(self):
        return self.solde - self.conge.days

    @property
    def days(self):
        return self.conge.days

from django.db import models
from django.utils import timezone


class Formation(models.Model):
    titre = models.CharField(max_length=200, blank=False, default="")
    genre = models.CharField(max_length=200, blank=False, default="")
    jour = models.DateField(
        blank=True, default=timezone.now)
    formateur = models.CharField(max_length=200, blank=False, default="")
    duree = models.IntegerField(default=1)
    lieu = models.CharField(max_length=200, blank=False, default="")
    sujet = models.CharField(max_length=300, blank=False, default="")

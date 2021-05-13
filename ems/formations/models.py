from django.db import models
from django.utils import timezone


class Formation(models.Model):
    titre = models.CharField(max_length=200, blank=False)
    genre = models.CharField(max_length=200, blank=False)
    jour = models.DateField(
        blank=True, default=timezone.now)
    formateur = models.CharField(max_length=200, blank=False)
    duree = models.IntegerField(default=1)
    lieu = models.CharField(max_length=200, blank=False)
    sujet = models.CharField(max_length=300, blank=False)

from django.db import models
from django.utils import timezone


class Recruitment(models.Model):
    POSTE = [
        ("FT", 'Temps plein'),
        ("PT", 'Temp partiel'),
        ("ST", 'Sous-traitant'),
        ("S", 'Stagiaire'),
    ]

    direction = models.CharField(max_length=100, blank=False)
    responsable = models.CharField(max_length=100, blank=False)
    date_demande = models.DateField(default=timezone.now)
    poste = models.CharField(max_length=100, blank=False)
    poste_type = models.CharField(
        max_length=100, choices=POSTE, default=POSTE[0][0])
    poste_description = models.TextField()
    motivation = models.TextField()
    exp_requise = models.TextField()
    formation_requise = models.TextField()

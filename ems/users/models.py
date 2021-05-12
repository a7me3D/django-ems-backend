from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils import timezone


class Employee(AbstractUser):
    ROLE = [
        ("S", 'Salarie'),
        ("RI", 'Responsable Informatique'),
        ("CH", 'Chef Hierarchique'),
        ("RF", 'Responsable Financier'),
        ("RH", 'Responsable ressources Humaines'),
    ]

    SEXE = [
        ("H", "Homme"),
        ("F", "Femme")
    ]
    adresse = models.CharField(max_length=300, blank=True)
    ville = models.CharField(max_length=100, blank=True)
    code_postal = models.CharField(max_length=100, blank=True)
    nationnalite = models.CharField(max_length=200, blank=True)
    cin = models.CharField(max_length=15, blank=True)
    date_naissance = models.DateField(
        blank=True, default=timezone.now)
    lieu_naissance = models.CharField(max_length=300, blank=True)
    email = models.EmailField(blank=True, unique=True)
    chef = models.ForeignKey(
        "self", on_delete=models.CASCADE, null=True, related_name="hierarchy_chef")
    poste = models.CharField(max_length=2, choices=ROLE, default=ROLE[0][0])
    sexe = models.CharField(max_length=1, choices=SEXE, default=SEXE[0][0])

    USERNAME_FIELD = 'email'

    username = None
    REQUIRED_FIELDS = []

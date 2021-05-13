from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils import timezone
from evaluations.models import Evaluation


class Employee(AbstractUser):
    ROLE = [
        ("S", 'Salarie'),
        ("RI", 'Responsable Informatique'),
        ("RF", 'Responsable Financier'),
        ("RH", 'Responsable ressources Humaines'),
    ]

    SEXE = [
        ("H", "Homme"),
        ("F", "Femme")
    ]
    adresse = models.CharField(max_length=300)
    ville = models.CharField(max_length=100)
    code_postal = models.CharField(max_length=100)
    nationnalite = models.CharField(max_length=200)
    cin = models.CharField(max_length=15)
    date_naissance = models.DateField(
        default=timezone.now)
    lieu_naissance = models.CharField(max_length=300)
    email = models.EmailField(unique=True)
    poste = models.CharField(max_length=2, choices=ROLE, default=ROLE[1][0])
    sexe = models.CharField(max_length=1, choices=SEXE, default=SEXE[0][0])

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ["username"]

    @property
    def evaluated(self):
        return Evaluation.objects.filter(employee__id=self.id).count()

    def save(self, *args, **kwargs):
        self.username = self.email
        super(Employee, self).save(*args, **kwargs)

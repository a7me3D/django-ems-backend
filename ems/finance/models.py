from django.db import models
from users.models import Employee


class FinanceDoc(models.Model):
    DOC_TYPE = [
        ("DP", "Demande de prêt"),
        ("DA", "Demande d'avance sur salaire")
    ]

    STATUS_TYPE = [
        ("P", "En attente"),
        ("A", "Accepté"),
        ("R", "Refusé"),
    ]
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    doc_type = models.CharField(max_length=2,
                                choices=DOC_TYPE, default=DOC_TYPE[0][0], null=False, blank=False)
    montant = models.DecimalField(
        null=False, blank=False, decimal_places=3, max_digits=6)
    motif = models.TextField(null=False, blank=False)
    nb_echeances = models.IntegerField(null=False, blank=False)
    avis_rf = models.BooleanField()
    status = models.CharField(
        max_length=2, choices=STATUS_TYPE, default=STATUS_TYPE[0][0])

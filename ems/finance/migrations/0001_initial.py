# Generated by Django 3.2 on 2021-05-13 05:30

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='FinanceDoc',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('doc_type', models.CharField(choices=[('DP', 'Demande de prêt'), ('DA', "Demande d'avance sur salaire")], default='DP', max_length=2)),
                ('montant', models.DecimalField(decimal_places=3, max_digits=6)),
                ('motif', models.TextField()),
                ('nb_echeances', models.IntegerField()),
                ('avis_rf', models.BooleanField()),
                ('status', models.CharField(choices=[('P', 'En attente'), ('A', 'Accepté'), ('R', 'Refusé')], default='P', max_length=2)),
            ],
        ),
    ]

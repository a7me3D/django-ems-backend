# Generated by Django 3.2 on 2021-05-13 05:30

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Recruitment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('direction', models.CharField(max_length=100)),
                ('responsable', models.CharField(max_length=100)),
                ('date_demande', models.DateField(default=django.utils.timezone.now)),
                ('poste', models.CharField(max_length=100)),
                ('poste_type', models.CharField(choices=[('FT', 'Temps plein'), ('PT', 'Temp partiel'), ('ST', 'Sous-traitant'), ('S', 'Stagiaire')], default='FT', max_length=100)),
                ('poste_description', models.TextField()),
                ('motivation', models.TextField()),
                ('exp_requise', models.TextField()),
                ('formation_requise', models.TextField()),
            ],
        ),
    ]

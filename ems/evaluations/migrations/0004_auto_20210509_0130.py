# Generated by Django 3.2 on 2021-05-09 00:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('evaluations', '0003_auto_20210509_0117'),
    ]

    operations = [
        migrations.CreateModel(
            name='CriteriaType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
            ],
        ),
        migrations.AlterField(
            model_name='criteria',
            name='title',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='evaluations.criteriatype'),
        ),
    ]
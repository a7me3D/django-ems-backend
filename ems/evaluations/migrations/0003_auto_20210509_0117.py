# Generated by Django 3.2 on 2021-05-09 00:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('evaluations', '0002_auto_20210509_0116'),
    ]

    operations = [
        migrations.AlterField(
            model_name='criteria',
            name='comment',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='criteria',
            name='rating',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
# Generated by Django 3.2 on 2021-05-13 04:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('evaluations', '0004_auto_20210509_0130'),
    ]

    operations = [
        migrations.AlterField(
            model_name='criteria',
            name='comment',
            field=models.TextField(default=' '),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='criteria',
            name='rating',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]

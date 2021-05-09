# Generated by Django 3.2 on 2021-05-09 00:09

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0006_remove_employee_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='chef',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='hierarchy_chef', to=settings.AUTH_USER_MODEL),
        ),
    ]

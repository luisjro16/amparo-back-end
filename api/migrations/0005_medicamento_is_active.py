# Generated by Django 5.1.7 on 2025-06-22 15:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_agendamento_data_fim'),
    ]

    operations = [
        migrations.AddField(
            model_name='medicamento',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
    ]

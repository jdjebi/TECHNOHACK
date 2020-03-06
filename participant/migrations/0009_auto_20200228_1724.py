# Generated by Django 3.0.3 on 2020-02-28 17:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('participant', '0008_participant_is_chief'),
    ]

    operations = [
        migrations.AlterField(
            model_name='equipe',
            name='salle',
            field=models.CharField(blank=True, choices=[('RTEL 1', 'RTEL 1'), ('RTEL 2', 'RTEL 2'), ('SRIT2 A', 'SRIT2 A'), ('SRIT2 B', 'SRIT2 B'), ('SRIT3 A', 'SRIT3 A')], default='', max_length=20, null=True),
        ),
    ]
# Generated by Django 4.2.11 on 2024-12-21 14:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pokedex', '0002_trainer_alter_pokemon_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pokemon',
            name='type',
            field=models.CharField(choices=[('A', 'Agua'), ('T', 'Tierra'), ('E', 'Eléctrico'), ('P', 'Planta'), ('L', 'Lagartija'), ('F', 'Fuego')], max_length=30),
        ),
    ]

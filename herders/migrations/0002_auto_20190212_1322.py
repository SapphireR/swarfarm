# Generated by Django 2.1.5 on 2019-02-12 21:22

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('herders', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='runeinstance',
            name='substat_craft_values',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.IntegerField(), blank=True, null=True, size=4),
        ),
        migrations.AlterField(
            model_name='runeinstance',
            name='substat_values',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.IntegerField(blank=True, null=True), default=list, size=4),
        ),
        migrations.AlterField(
            model_name='runeinstance',
            name='substats',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.IntegerField(blank=True, choices=[(1, 'HP'), (2, 'HP %'), (3, 'ATK'), (4, 'ATK %'), (5, 'DEF'), (6, 'DEF %'), (7, 'SPD'), (8, 'CRI Rate %'), (9, 'CRI Dmg %'), (10, 'Resistance %'), (11, 'Accuracy %')], null=True), default=list, size=4),
        ),
    ]
